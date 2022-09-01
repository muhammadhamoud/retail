==========================
|$project|'s Documentation
==========================
.. image:: http://unmaintained.tech/badge.svg
  :target: http://unmaintained.tech
  :alt: No Maintenance Intended

.. |$project| replace:: emeamarsha

Provides a complete Integrated Development Environment to automate Marsha commands
The BlueZone Host Automation Object is a Component Object Model (COM) software component for 32-bit Windows platforms.

.. code-block:: python

    for i in range(10):
        print(i)

    print('Explicit is better than implicit.')

* this is only one way of addin text


*Note: This template is not maintained anymore,
use the* `tutorial <https://github.com/readthedocs/tutorial-template/>`_ *instead.*

$project will solve your problem of where to start with documentation,
by providing a basic explanation of how to do it easily.

Look how easy it is to use:

    import project
    # Get your stuff done
    project.do_stuff()

    test data

⚠️ Features
--------

- Be awesome
- Make things faster

Installation
------------

Install |$project| by running:

    pip install |$project|

Contribute
----------
If you plan to contribute for use in the documentation, see the `Guidelines for contributing <CONTRIBUTING.md>`_. 
- Issue Tracker: github.com/|$project|/|$project|/issues
- Source Code: github.com/|$project|/|$project|

Support
-------

If you are having issues, please let us know.
If you'd like to chat with the developer(s) or other users in the community, freel free to join the Gitter channel:
`Gitter Community <https://gitter.im/emeamarsha/community>`_


License
-------

The project is licensed under the MIT license.




Tutorial on managing a project
==============================

This tutorial will teach you to manage a project, and publish it on PyPI. 
This guide is majorly influenced by the following `tutorial
<https://blog.ionelmc.ro/2014/05/25/python-packaging/>`_.

Also, this tutorial will always be a work in progress (or at least so long
as best practice can change), so the tutorial might change at any time.
However, you can always read old versions of the tutorial,  since it is
covered by source control. Finally, if you have any constructive critic on the
contents in this tutorial, please raise an Issue with the Issue tracker.

Table of contents
-----------------

contents:: 


Structuring a repository
------------------------
An integral part of having reusable code is having a sensible repository
structure. That is, which files do we have and how do we organise them.
Unfortunately, figuring out how to structure a Python project best is not
a trivial task. In this part of the tutorial, I hope to show you a way
to initate any Python project to ensure that you won't have to do major
effort restructuring the code once you want to publish it.  

Let us start with the folder layout. Your project directory should
be structured in the following way and we will explain why later.

.. code-block:: raw
   
   project_name
   ├── docs
   │   ├── make.bat
   │   ├── Makefile
   │   └── source
   │       ├── conf.py
   │       └── index.rst
   ├── examples
   │   └── example.py
   ├── src
   │   └── package_name
   │       └── __init__.py
   ├── tests
   │   └── __init__.py
   ├── .gitignore
   ├── LICENSE.txt
   ├── MANIFEST.in
   ├── README.rst
   ├── requirements.txt
   ├── setup.cfg
   ├── setup.py
   └── tox.ini

Now, this is a lot of files, let us look at these to understand what the
different components are and why they are necessary in a Python project.

The ``setup`` files
^^^^^^^^^^^^^^^^^^^

The ``setup.py``, ``setup.cfg`` and ``MANIFEST.in`` files are used to
specify how a package should be installed. You might think that you don't
want to create an installable package, so let's skip this. DON'T! Even for
small projects, you should include these because of something called
editable installs (more on that later). The most basic setup.py file should
look like this

.. code-block:: python

   from setuptools import setup

   setup()

Some projects might include more code, especially if you are using Cython
or creating C-extensions to Python. However, if you are not, then this style
will probably suffice. The reason we keep the ``setup.py`` minimal is that
we want to keep as much of the setup configuration as possible inside the
``setup.cfg`` file. This is to let other people parse metadata about our
package without running a Python file first! The ``setup.cfg`` file should
look like this

.. code-block:: ini

   [metadata]      
   name = <package-name>
   version = <version number: 0.0.0>
   license = <license name, e.g. MIT>    
   description = <A short description>
   long_description = file: README.rst
   author = <Author name>
   author_email = <Optional: author e-mail>
   classifiers=
      <classifier 1>
      <classifier 2>
      <...>
      <classifier m>
            
   [options]
   packages = find:
   package_dir = 
       =src
   include_package_data = True
   install_requires = 
      <requirement 1>
      <requirement 2>
      <...>
      <requirement n>

   [options.packages.find]
   where=src

This file is formated according to `this
<https://setuptools.readthedocs.io/en/latest/setuptools.html#configuring-setup-using-setup-cfg-files>`_
specification. However, if you you
simply follow the layout above, replacing the elements wrapped in ``<>`` with
the correct information for your package, then you are ok.

There are two sections here that might be confusing, the ``classifiers``
section and the ``install_requires`` section. The ``classifiers`` section is
used by PyPI to make it easier for new users to find your package, you can find a full list of classifiers `here
<https://pypi.org/classifiers/>`_. Likewise, the
``install_requires`` section specifies which Python packages that ``pip`` should
install before installing the package you are developing. Both these fields are
optional, so you can leave them blank until you have anything to fill in.

Lastly, the ``MANIFEST.in`` file. This file is used to instruct setupttools
on which files it should include when it creates an installable project. For
a general project, I reccomend having a file with the following layout.

.. code-block:: raw

   include setup.py
   include MANIFEST.in
   include LICENSE
   include README.md

   graft tests
   graft examples
   graft docs
   graft src

The ``requirements.txt`` file 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``requirements.txt`` file is similar to the ``install_requires`` field in
the ``setup.cfg`` file we described above. However, the aim of the
``requirements.txt`` file is not to specify the dependencies of your package,
but the packages needed to work on developing your package. Each dependency
should be on a separate line. Here is an example of a ``requirements.txt``
file.

.. code-block:: raw

   scikit-learn
   tox
   black
   isort
   -e .

We will depend on ``scikit-learn`` if we are to create scikit-learn compliant
code. Similarly, we need ``tox`` to run our test-suite. ``black`` and ``isort``
are two really good code auto-formatters, which you can read more about on
their GitHub pages (`black
<https://github.com/psf/black>`_ and `isort
<https://github.com/timothycrosley/isort>`_). Finally, with the ``-e .`` line
we install the current directory in editable mode.

The ``README.rst`` file
^^^^^^^^^^^^^^^^^^^^^^^^
The readme file contains the contens that are showed by default on online
source control providers such as GitHub, GitLab and BitBucket. Normally, this
is formatted as a Markdown file. However, I reccomend that you use
reStructuredText (rst) instead, since that is the file-format used by Sphinx,
the most commonly used auto-documentation tool for Python.

Additionally, PyPI will only host rst formatted help strings, not Markdown
formatted ones. Thus, if you wish to make your library public for ``pip``
installation in the future, then you should use rst to avoid writing the
same text twice.

The rst documentation is available `here
<http://docutils.sourceforge.net/docs/user/rst/quickstart.html>`_, and a good
summary is available `here
<https://github.com/ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst>`_.


The ``.gitignore`` file
^^^^^^^^^^^^^^^^^^^^^^^^

The ``.gitignore`` file contains instructions to Git, informing it of which
files it should not track. Examples of such files are the ``__pycache__`` files
and IDE configuration files. You can either copy the ``.gitignore`` file in this
repository, which should work for a large array of development environments, or
create your own ``.gitignore`` using `gitignore.io
<http://gitignore.io/>`_.

The ``LICENSE.txt`` file
^^^^^^^^^^^^^^^^^^^^^^^^

Your project needs an open source license, otherwise, noone will be able to use
your project. I like the MIT license, which is a very open license. To decide a 
license, i reccomend `choosealicense
<https://choosealicense.com/>`_ if
you are unsure as to which license to use.

Running tests with tox
^^^^^^^^^^^^^^^^^^^^^^

You should unit test your code. Otherwise there will be bugs, no matter how
simple the codebase is. The tool I like to use for unit testing is called
tox, and works by creating new virtual environments for each python version
you want to test the codebase with. It then installs all libraries necessary
to run the test suite before running it. These specifications are given in the
``tox.ini`` file, which can have the following structure

.. code-block:: ini

   [tox]
   envlist = 
      py35
      py36

   [testenv]
   deps =
      pytest
      pytest-cov
      pytest-randomly
   commands =
       pytest --cov=<package_name> --randomly-seed=1

The ``envlist`` field specifies which python versions to run the code with,
the ``deps`` field specifies the test dependencies (which might be different
from the devloper dependencies) and ``commands`` specifies which commands to
be ran to run the test suite.

NOTE: tox with conda
""""""""""""""""""""
Note that ``tox`` by itself doesn't play nice with ``conda``. Thus, if you
have an Anaconda or Miniconda installation of Python, then you should manually
install ``tox-conda`` through ``pip``.
    
Keeping the package source in the src folder
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You might have noticed that the source files are kept inside a separate ``src``
folder. The reason is that we should be certain that the code we are testing
is the installable code. To accomplish this, it is neccessary to structure the
code this way. For more information on this topic, see `this page
<https://hynek.me/articles/testing-packaging/#src>`_.

Keeping the tests in a tests folder
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For the same reason as we keep the package source in the src folder, we keep the
unit tests in the tests folder.

Documenting the code with sphinx
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When you publish code, you should also publish documentation to that code, and
creating the documentation is very simple if you have good docstrings and use
`sphinx
<http://www.sphinx-doc.org/en/master/>`_. To use sphinx, navigate to the docs
folder in the terminal window and type sphinx-quickstart.

We will not discuss sphinx in detail here, the only extra note I want to add
is to use the `sphinx.ext.napoleon` extension so your docstrings can be in the
`numpydoc
<https://github.com/numpy/numpydoc>`_ style.

Providing example code
^^^^^^^^^^^^^^^^^^^^^^

Any library should come with at least a minimal example script so prospective
users can see how the package was intended to be used. Keep these example
scripts in the examples folder.

Editable installs
-----------------
One immensely useful facet of the python ecosystem is editable installs. Often,
when new Python programmers create a project, they do not install the project
with pip. Rather, whenever they need to use the code from one project within
another, they end up manually modifying the system path environment variable.
If this sounds familiar, then you should stop that immediately. There is a
cleaner, easier and less error-prone way to accomplish the same. This way is
called editable installs.

Normally when we install a Python package, it is copied into the 
``site-packages`` directory. This is not ideal if the code we installed
is code that we are actively developing. In this case, we want to create a
symbolic link between the ``site-packages`` directory and the project
directory, and a way to accomplish this is through editable installs.

To installl a project in editable mode, simply navigate to the project root
directory and type ``pip install -e .`` in the terminal window. A benefit of
doing it this way, is that we have better cross-platform support. Windows and
UNIX based systems have vastly different ways of handling the path variable, so
your old ``sys.path.append`` hack might not work as intended on a Windows
machine. Additionally, the ``sys.path.append`` method is highly dependent on the
file-structure on your computer, whereas editable installs are not.


Automatic documentation
-----------------------

The second most important part of a project, after the source code itself, is
the documentation. Luckily, writing Python documentation is relatively painless
so long as you write your docstrings following the Sphinx guidelines. I will
assume that you have a working sphinx environment and simply want to host the
documentation somewhere.

If you are in this category, then you are in luck since you can host your
documentation for free on `Read the Docs
<https://readthedocs.org/>`_. To do this, you need to connect your GitHub
user to `https://readthedocs.org` (note the org top level domain (TLD), not
an io TLD). Once you have connected your GitHub to Read the Docs, you need
to add the ``.readthedocs.yml`` file to your repository. This file should have
the following lines in it.

.. code-block:: yaml

   python:
      setup_py_install: true

After adding the ``.readthedocs.yml`` file to the repository, it should have
the following layout.

.. code-block:: raw
   
   project_name
   ├── docs
   │   ├── make.bat
   │   ├── Makefile
   │   └── source
   │       ├── conf.py
   │       └── index.rst
   ├── examples
   │   └── example.py
   ├── src
   │   └── package_name
   │       └── __init__.py
   ├── tests
   │   └── test_package_name
   │       └── __init__.py
   ├── .gitignore
   ├── .readthedocs.yml  <- This file is new
   ├── LICENSE.txt
   ├── MANIFEST.in
   ├── README.rst
   ├── requirements.txt
   ├── setup.cfg
   ├── setup.py
   └── tox.ini

Once it does, you can import the project to Read the Docs, by pressing the
"Import a Project" button and choosing the correct GitHub repository.

You might want to have a badge that shows whether your documentation builds
correctly on your GitHub page, to do this, press the "i" button on the right
of the green "docs passing" badge (or red "docs failing" if your documentation
isn't building correctly). Copy the rst code to somewhere near the beginning of your readme file. The code should be on the following form:

.. code-block:: raw

   .. image:: https://readthedocs.org/projects/<repo_name>/badge/?version=latest
      :target: https://<repo_name>.readthedocs.io/en/latest/?badge=latest
      :alt: Documentation Status

Using continuous integration
----------------------------

Another useful tool when developing code is a continuous integration tool.
Such tools will automatically run the unit tests on activity to the GitHub
repository. Luckily, there exists a very good tool called `*Travis-CI*
<https://travis-ci.org/>`_, which is free for all open source projects.

To use Travis-CI, you must link your GitHub user to Travis CI on their webpage.
After this, you simply choose which repository to activate Travis for and you
are set to go. When you have activated Travis for a specific repo, you need
to add a ``.travis.yml`` file to the project root, giving you the following
file structure

.. code-block:: raw
   
   project_name
   ├── docs
   │   ├── make.bat
   │   ├── Makefile
   │   └── source
   │       ├── conf.py
   │       └── index.rst
   ├── examples
   │   └── example.py
   ├── src
   │   └── package_name
   │       └── __init__.py
   ├── tests
   │   └── test_package_name
   │       └── __init__.py
   ├── .gitignore
   ├── .readthedocs.yml
   ├── .travis.yml  <- This file is new
   ├── LICENSE.txt
   ├── MANIFEST.in
   ├── README.rst
   ├── requirements.txt
   ├── setup.cfg
   ├── setup.py
   └── tox.ini

The contents of the ``.travis.yml`` file should be the following

.. code-block:: yaml

   sudo: false
   language: python
   python:
     - "3.7"
   # command to install dependencies
   install:
   before_script:
     - pip install tox-travis
   # command to run tests
   script: tox

This file will ensure that tox is run on Travis-CI any time someone pushes
a change to the GitHub repository. You might also want to add a badge to
your readme file. To do this, navigate to the Travis-CI dashboard, press
the link to the repository that you want to add the badge for, press the
badge showing ``build passing`` (ideally, it will show ``build failing``
if your tests are failing) and finally, choose rst from the bottom dropdown
menu. Once you have done this, copy the text in the text-box and paste it
somewhere around the top of yor ``README.rst`` file. The rst code that you
copy should look something like this

.. code-block:: rst

   .. image:: https://travis-ci.org/<github_username>/<repo_name>.svg?branch=<branch_name>
      :target: https://travis-ci.org/<github_username>/<repo_name>


Automatic coverage reporting
----------------------------

Another useful tool in a programmer's arsenal is automatic code coverage
reporting. Have you ever seen a repository where they have a badge that
shows how high their code-coverage is with a small badge? They accomplish
this using one of many automatic code-coverage reporters. Personally,
I like to use `*Coveralls*
<https://coveralls.io/>`_, which has a relatively easy-to-use interface
and integrates well with Travis-CI.

To start using Coveralls, you must first register and link your GitHub account
with Coveralls. Once you have done that, you need to add your repository to
Coveralls. You can do this, by pressing the plus button on the left-hand side of
the Coveralls dashboard and enable whichever repository you want. Once you have
done this, you must update the ``.travis.yml`` file so Coveralls are ran after
the test suite. The new ``.travis.yml`` file should look like this:

.. code-block:: yaml

   sudo: false
   language: python
   python:
     - "3.7"
   # command to install dependencies
   install:
   before_script:
     - pip install tox-travis
     - pip install coveralls
   # command to run tests
   script: tox
   after_success: coveralls

Once you have made this update, then Coveralls will run after travis. Next, you
want to add the coverage badge to your ``README.rst`` file. In the Coveralls
project dashboard, you should see a badge that displays your code coverage,
press the embed button on the top right corner near the badge and copy the
code for rst into your ``README.rst`` file. The code you copy should have
the following format

.. code-block:: rst

   .. image:: https://coveralls.io/repos/github/<github_username>/<repo_name>/badge.svg?branch=<branch_name>
      :target: https://coveralls.io/github/<github_username>/<repo_name>?branch=<branch_name>

Uploading to PyPI
-----------------
It is finally time to upload our code to PyPI, making it easily installable for
others. Uploading code to PyPI is very simple. First, create an account on PyPI.
Then, you need to install two packages; twine and wheel. To do this, write 
``pip install twine wheel`` in the terminal window. Then, navigate to the
project root and type ``python setup.py sdist bdist_wheel``, this will prepare
your package for uploading to PyPI. Then, write ``twine upload dist/*`` to
upload your project.




Sample Binary Tree Library
##########################

.. image:: https://github.com/shunsvineyard/python-sample-code/workflows/Test/badge.svg
    :target: https://github.com/shunsvineyard/python-sample-code/actions?query=workflow%3ATest

.. image:: https://github.com/shunsvineyard/python-sample-code/workflows/Linting/badge.svg 
    :target: https://github.com/shunsvineyard/python-sample-code/actions?query=workflow%3ALinting

.. image:: https://codecov.io/gh/shunsvineyard/python-sample-code/branch/main/graph/badge.svg?token=zLkKU6p7do
    :target: https://codecov.io/gh/shunsvineyard/python-sample-code
    
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black


The **Binary Tree Library** is a Python sample project used by shunsvineyard.info. It is an example for `Sphinx <https://www.sphinx-doc.org/>`_ and `My Python Coding Style <https://shunsvineyard.info/2019/01/05/my-python-coding-style-and-principles/>`_.

Although it is a sample project, the **Binary Tree Library** is a usable tree data structure library, and has the following tree data structures:

- AVL Tree
- Binary Search Tree
- Red Black Tree
- Threaded Binary Trees

The library also provides the tree traversal feature to traverse binary trees.

- Binary Tree Traversal
    - In-order
    - Reversed In-order
    - Pre-order
    - Post-order
    - Level-order

Requirements
------------

The **Binary Tree Library** requires Python 3.7 or newer.
The key Python 3.7 feature used in the project is `dataclass <https://docs.python.org/3/library/dataclasses.html#module-dataclasses>`_.

Installation
------------

Install from Github

.. code-block:: text

    git clone https://github.com/shunsvineyard/python-sample-code.git
    cd python-sample-code
    pip install .

Examples
--------

.. code-block:: python

    from trees import tree_exceptions
    from trees.binary_trees import red_black_tree
    from trees.binary_trees import traversal


    class Map:
        def __init__(self):
            self._rbt = red_black_tree.RBTree()

        def __setitem__(self, key, value):
            self._rbt.insert(key=key, data=value)

        def __getitem__(self, key):
            return self._rbt.search(key=key).data

        def __delitem__(self, key):
            self._rbt.delete(key=key)

        def __iter__(self):
            return traversal.inorder_traverse(tree=self._rbt)


    if __name__ == "__main__":

        # Initialize the Map instance.
        contacts = Map()

        # Add some items.
        contacts["Mark"] = "mark@email.com"
        contacts["John"] = "john@email.com"
        contacts["Luke"] = "luke@email.com"
        contacts["john"] = "john@email.com"

        # Iterate the items.
        for contact in contacts:
            print(contact)

        # Delete one item.
        del contacts["john"]

        # Check the deleted item.
        try:
            print(contacts["john"])
        except tree_exceptions.KeyNotFoundError:
            print("john does not exist")


Tree CLI
--------

The **Binary Tree Library** provides a command line tool to simulate tree data structures.

.. code-block:: text

    tree-cli

It will show the interactive prompt. Use ``help`` to list all the available commands


.. code-block:: text

    Welcome to the Tree CLI. Type help or ? to list commands.

    tree> help

    Documented commands (type help <topic>):
    ========================================
    build  delete  destroy  detail  exit  help  insert  search  traverse





This module illustrates how to write your docstring in OpenAlea
and other projects related to OpenAlea.

__license__ = "Cecill-C"
__revision__ = " $Id: actor.py 1586 2009-01-30 15:56:25Z cokelaer $ "
__docformat__ = 'reStructuredText'


class MainClass1(object):
    """This class docstring shows how to use sphinx and rst syntax

    The first line is brief explanation, which may be completed with 
    a longer one. For instance to discuss about its methods. The only
    method here is :func:`function1`'s. The main idea is to document
    the class and methods's arguments with 

    - **parameters**, **types**, **return** and **return types**::

          :param arg1: description
          :param arg2: description
          :type arg1: type description
          :type arg1: type description
          :return: return description
          :rtype: the return type description

    - and to provide sections such as **Example** using the double commas syntax::

          :Example:

          followed by a blank line !

      which appears as follow:

      :Example:

      followed by a blank line

    - Finally special sections such as **See Also**, **Warnings**, **Notes**
      use the sphinx syntax (*paragraph directives*)::

          .. seealso:: blabla
          .. warnings also:: blabla
          .. note:: blabla
          .. todo:: blabla

    .. note::
        There are many other Info fields but they may be redundant:
            * param, parameter, arg, argument, key, keyword: Description of a
              parameter.
            * type: Type of a parameter.
            * raises, raise, except, exception: That (and when) a specific
              exception is raised.
            * var, ivar, cvar: Description of a variable.
            * returns, return: Description of the return value.
            * rtype: Return type.

    .. note::
        There are many other directives such as versionadded, versionchanged,
        rubric, centered, ... See the sphinx documentation for more details.

    Here below is the results of the :func:`function1` docstring.

    """

    def function1(self, arg1, arg2, arg3):
        """returns (arg1 / arg2) + arg3

        This is a longer explanation, which may include math with latex syntax
        :math:`\\alpha`.
        Then, you need to provide optional subsection in this order (just to be
        consistent and have a uniform documentation. Nothing prevent you to
        switch the order):

          - parameters using ``:param <name>: <description>``
          - type of the parameters ``:type <name>: <description>``
          - returns using ``:returns: <description>``
          - examples (doctest)
          - seealso using ``.. seealso:: text``
          - notes using ``.. note:: text``
          - warning using ``.. warning:: text``
          - todo ``.. todo:: text``

        **Advantages**:
         - Uses sphinx markups, which will certainly be improved in future
           version
         - Nice HTML output with the See Also, Note, Warnings directives


        **Drawbacks**:
         - Just looking at the docstring, the parameter, type and  return
           sections do not appear nicely

        :param arg1: the first value
        :param arg2: the first value
        :param arg3: the first value
        :type arg1: int, float,...
        :type arg2: int, float,...
        :type arg3: int, float,...
        :returns: arg1/arg2 +arg3
        :rtype: int, float

        :Example:

        >>> import template
        >>> a = template.MainClass1()
        >>> a.function1(1,1,1)
        2

        .. note:: can be useful to emphasize
            important feature
        .. seealso:: :class:`MainClass2`
        .. warning:: arg2 must be non-zero.
        .. todo:: check that arg2 is non zero.
        """




|RST|_ is a little annoying to type over and over, especially
when writing about |RST| itself, and spelling out the
bicapitalized word |RST| every time isn't really necessary for
|RST| source readability.


.. _RST: http://docutils.sourceforge.net/rst.html



Abstract
========

[A short (~200 word) description of the technical issue being addressed.]


Motivation
==========

[Clearly explain why the existing language specification is inadequate to address the problem that the PEP solves.]


Rationale
=========

[Describe why particular design decisions were made.]


Specification
=============

[Describe the syntax and semantics of any new language feature.]


Backwards Compatibility
=======================

[Describe potential impact and severity on pre-existing code.]


Security Implications
=====================

[How could a malicious user take advantage of this new feature?]


How to Teach This
=================

[How to teach users, new and experienced, how to apply the PEP to their work.]


Reference Implementation
========================

[Link to any existing implementation and details about its state, e.g. proof-of-concept.]


Rejected Ideas
==============

[Why certain ideas that were brought while discussing this PEP were not ultimately pursued.]


Open Issues
===========

[Any points that are still being decided/discussed.]


Footnotes
=========

[A collection of footnotes cited in the PEP, and a place to list non-inline hyperlink targets.]


Copyright
=========

This document is placed in the public domain or under the
CC0-1.0-Universal license, whichever is more permissive.




=====================================================
 The reStructuredText_ Cheat Sheet: Syntax Reminders
=====================================================
:Info: See <https://docutils.sourceforge.io/rst.html> for introductory docs.
:Author: David Goodger <goodger@python.org>
:Date: $Date: 2022-01-20 11:11:44 +0100 (Do, 20. JÃ¤n 2022) $
:Revision: $Revision: 8956 $
:Description: This is a "docinfo block", or bibliographic field list

.. NOTE:: If you are reading this as HTML, please read
   `<cheatsheet.txt>`_ instead to see the input syntax examples!

Section Structure
=================
Section titles are underlined or overlined & underlined.

Body Elements
=============
Grid table:

+--------------------------------+-----------------------------------+
| Paragraphs are flush-left,     | Literal block, preceded by "::":: |
| separated by blank lines.      |                                   |
|                                |     Indented                      |
|     Block quotes are indented. |                                   |
+--------------------------------+ or::                              |
| >>> print 'Doctest block'      |                                   |
| Doctest block                  | > Quoted                          |
+--------------------------------+-----------------------------------+
| | Line blocks preserve line breaks & indents. [new in 0.3.6]       |
| |     Useful for addresses, verse, and adornment-free lists; long  |
|       lines can be wrapped with continuation lines.                |
+--------------------------------------------------------------------+

Simple tables:

================  ============================================================
List Type         Examples (syntax in the `text source <cheatsheet.txt>`_)
================  ============================================================
Bullet list       * items begin with "-", "+", or "*"
Enumerated list   1. items use any variation of "1.", "A)", and "(i)"
                  #. also auto-enumerated
Definition list   Term is flush-left : optional classifier
                      Definition is indented, no blank line between
Field list        :field name: field body
Option list       -o  at least 2 spaces between option & description
================  ============================================================

================  ============================================================
Explicit Markup   Examples (visible in the `text source`_)
================  ============================================================
Footnote          .. [1] Manually numbered or [#] auto-numbered
                     (even [#labelled]) or [*] auto-symbol
Citation          .. [CIT2002] A citation.
Hyperlink Target  .. _reStructuredText: https://docutils.sourceforge.io/rst.html
                  .. _indirect target: reStructuredText_
                  .. _internal target:
Anonymous Target  __ https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html
Directive ("::")  .. image:: images/biohazard.png
Substitution Def  .. |substitution| replace:: like an inline directive
Comment           .. is anything else
Empty Comment     (".." on a line by itself, with blank lines before & after,
                  used to separate indentation contexts)
================  ============================================================

Inline Markup
=============
*emphasis*; **strong emphasis**; `interpreted text`; `interpreted text
with role`:emphasis:; ``inline literal text``; standalone hyperlink,
https://docutils.sourceforge.io; named reference, reStructuredText_;
`anonymous reference`__; footnote reference, [1]_; citation reference,
[CIT2002]_; |substitution|; _`inline internal target`.

Directive Quick Reference
=========================
See <https://docutils.sourceforge.io/docs/ref/rst/directives.html> for full info.

================  ============================================================
Directive Name    Description (Docutils version added to, in [brackets])
================  ============================================================
attention         Specific admonition; also "caution", "danger",
                  "error", "hint", "important", "note", "tip", "warning"
admonition        Generic titled admonition: ``.. admonition:: By The Way``
image             ``.. image:: picture.png``; many options possible
figure            Like "image", but with optional caption and legend
topic             ``.. topic:: Title``; like a mini section
sidebar           ``.. sidebar:: Title``; like a mini parallel document
parsed-literal    A literal block with parsed inline markup
rubric            ``.. rubric:: Informal Heading``
epigraph          Block quote with class="epigraph"
highlights        Block quote with class="highlights"
pull-quote        Block quote with class="pull-quote"
compound          Compound paragraphs [0.3.6]
container         Generic block-level container element [0.3.10]
table             Create a titled table [0.3.1]
list-table        Create a table from a uniform two-level bullet list [0.3.8]
csv-table         Create a table from CSV data [0.3.4]
contents          Generate a table of contents
sectnum           Automatically number sections, subsections, etc.
header, footer    Create document decorations [0.3.8]
target-notes      Create an explicit footnote for each external target
math              Mathematical notation (input in LaTeX format)
meta              Document metadata
include           Read an external reST file as if it were inline
raw               Non-reST data passed untouched to the Writer
replace           Replacement text for substitution definitions
unicode           Unicode character code conversion for substitution defs
date              Generates today's date; for substitution defs
class             Set a "class" attribute on the next element
role              Create a custom interpreted text role [0.3.2]
default-role      Set the default interpreted text role [0.3.10]
title             Set the metadata document title [0.3.10]
================  ============================================================

Interpreted Text Role Quick Reference
=====================================
See <https://docutils.sourceforge.io/docs/ref/rst/roles.html> for full info.

================  ============================================================
Role Name         Description
================  ============================================================
emphasis          Equivalent to *emphasis*
literal           Equivalent to ``literal`` but processes backslash escapes
math              Mathematical notation (input in LaTeX format)
PEP               Reference to a numbered Python Enhancement Proposal
RFC               Reference to a numbered Internet Request For Comments
raw               For non-reST data; cannot be used directly (see docs) [0.3.6]
strong            Equivalent to **strong**
sub               Subscript
sup               Superscript
title             Title reference (book, etc.); standard default role
================  ============================================================
