# -*- coding: utf-8 -*-

from __future__ import unicode_literals

"""
This module provides lemmatization functions based on an
external Unitex dictionary of flexed words.

This module doesn't consider words with hyphens inside them.
In the case of Portuguese (the original language the module was
developed for), this happens with clitic pronouns attached to
verbs. However, the module was targeted at systems using
Universal Dependencies, which treats verbs and clitics separately.
"""

import logging

unitex_dictionary = None
udtags2unitex = {'verb': 'V',
                 'aux': 'V',
                 'noun': 'N',
                 'adj': 'A'}
lemmatizable_delaf_tags = set(udtags2unitex.values())
lemmatizable_ud_tags = set(udtags2unitex.keys())


def load_unitex_dictionary(path):
    """
    Load the Unitex dictionary with inflected word forms.

    This function must be called before using `get_lemma`.
    :param path: the path to the unitex dictionary file
    """
    global unitex_dictionary

    logging.debug('Reading Unitex dictionary')
    with open(path, 'rb') as f:
        unitex_dictionary = {}
        for line in f:
            line = unicode(line, 'utf-8').strip()
            # each line is in the format
            # inflected_word,lemma.POS:additional_morphological_metadata
            # the morphological metadata is only available for open class words
            inflected, rest = line.split(',')
            if '-' in inflected:
                continue

            lemma, morph = rest.split('.')
            if ':' in morph:
                pos, _ = morph.split(':')
            else:
                pos = morph

            if pos not in lemmatizable_delaf_tags:
                continue

            unitex_dictionary[(inflected, pos)] = lemma


def get_lemma(word, pos, check_other_pos=True):
    """
    Retrieve the lemma of a word given its POS tag.

    If the combination of word and POS is not known, return the
    word itself.
    :param word: the word string
    :param pos: part of speech in Universal Treebanks standard
        (the only ones used are AUX, NOUN, VERB, ADJ; any other
        results in the lemma being the word itself)
    :param check_other_pos: if True and the combination of word and
        POS is not found in the Unitex dictionary, other POS tags
        will be tried.
    """
    global unitex_dictionary
    if unitex_dictionary is None:
        raise RuntimeError('Unitex dictionary was not loaded '
                           'before calling get_lemma')

    word = word.lower()
    pos = pos.lower()
    if pos not in lemmatizable_ud_tags:
        return word
    unitex_pos = udtags2unitex[pos]

    if (word, unitex_pos) not in unitex_dictionary:
        # a lot of times, this happens with signs like $ or %
        if len(word) == 1:
            return word

        # the POS tag could be wrong
        # but nouns and adjectives are more likely to be mistaken for each other
        if not check_other_pos:
            return word

        if unitex_pos == 'N':
            try_these = ['A', 'V']
        elif unitex_pos == 'A':
            try_these = ['N', 'V']
        else:
            try_these = ['N', 'A']

        for other_pos in try_these:
            if (word, other_pos) in unitex_dictionary:
                logging.debug('Could not find lemma for word {} with POS {},'
                              'but found for POS {}'.format(word, unitex_pos,
                                                            other_pos))
                return unitex_dictionary[(word, other_pos)]

        return word

    return unitex_dictionary[(word, unitex_pos)]
