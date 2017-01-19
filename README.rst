Unitex Lemmatizer
=================

This is a simple module for lemmatization based on the Unitex inflected word
list. As such, it needs a Unitex vocabulary file in order to work properly.

So far, I've only worked with Portuguese, with the
`DELAF_PB file <http://www.nilc.icmc.usp.br/nilc/projects/unitex-pb/web/dicionarios.html>`_
provided by NILC.

Installing
----------

You can either clone the repository and install with

.. code-block:: bash

    $ python setup.py install

or install through pip

.. code-block:: bash

    $ pip install unitexlemmatizer

Usage
-----

In order to use the Unitex Lemmatizer, you need to tell it where the word list
is:

.. code-block:: python

    >>> import unitexlemmatizer as ul
    >>> ul.load_unitex_dictionary('/path/to/delaf.dic')

Then, you can call the ``get_lemma`` function passing the inflected word and its
part of speech tag (from the `Universal Dependencies <http://universaldependencies.org>`_
tagset).

.. code-block:: python

    >>> ul.get_lemma('corpora', 'noun')
    'corpus'

