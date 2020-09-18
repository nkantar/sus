sus: Static URL Shortener
=========================

**sus** is a static site based URL shortener.
Simple idea: generate a static site with a bunch of
``redirect-slug-goes-here/index.html`` files with nothing but an HTML redirect in them.

.. image:: https://github.com/nkantar/sus/workflows/Automated%20Checks/badge.svg


Installation
------------

.. code-block:: sh

    pip install sus


Usage
-----

#. Install package
#. Have an ``input`` file ready
#. Run ``sus`` in the same directory as ``input``
#. Voilà—your results are in the ``output/`` directory


Input
-----

sus expects to find a file named ``input`` in the current directory, and each row
consists of the redirect slug and destination URL, separated by a pipe (``|``).

E.g.,

.. code-block::

    nk|https://nkantar.com
    sus|https://github.com/nkantar/sus

If I were serve the ``output/`` on `<https://sus-example.nkantar.com>`_, then
`<https://sus-example.nkantar.com/nk>`_ would redirect to `<https://nkantar.com>`_ and
`<https://sus-example.nkantar.com/sus>`_ would redirect to
`<https://github.com/nkantar/sus>`_.

Note: That example site exists, and its repository can be found at
`<https://github.com/nkantar/sus-example.nkantar.com>`_.


Development
-----------

The project by default uses `Poetry <https://python-poetry.org/>`_, and ``make install``
should get you up and running with all the dev dependencies.
After that see other ``make`` commands for convenience.
They correspond to CI checks required for changes to be merged in.

The ``main`` branch is the bleeding edge version.
`Git tags <https://github.com/nkantar/sus/tags>`_ correspond to releases.


Contributing Guidelines
-----------------------

Contributions of all sorts are welcome, be they bug reports, patches, or even just
feedback.
Creating a `new issue <https://github.com/nkantar/sus/issues/new>`_ or
`pull request <https://github.com/nkantar/sus/compare>`_ is probably the best way to get
started.

Please note that this project is released with a
`Contributor Code of Conduct <https://github.com/nkantar/sus/blob/master/CODE_OF_CONDUCT.md>`_.
By participating in this project you agree to abide by its terms.


License
-------

This project is licensed under the MIT license. See ``LICENSE`` file for details.
