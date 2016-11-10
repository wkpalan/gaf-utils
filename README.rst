gaf-utils
=========
|build_status| |requirement_status|

This is a simple python utility to read and write Gene Annotation Format Files. Will be updated to do more complicated filtering later on

## Package
Basic structure of package is
::

    ├── README.md
    ├── gaf
    │   ├── __init__.py
    │   └── gaf.py 
    ├── tests
    |   ├── __init__.py
    |   ├── test.gaf
    │   └── test_gaf.py
    ├── requirements.txt
    ├── setup.cfg
    └── setup.py
::

## Requirements

Package requirements are handled using pip. To install them do

```
pip install -r requirements.txt
```

.. |build_status| image:: https://api.travis-ci.org/wkpalan/gaf-utils.png?branch=master
.. _build_status_: https://travis-ci.org/wkpalan/gaf-utils

.. |requirement_status|  image:: https://requires.io/github/wkpalan/gaf-utils/requirements.svg?branch=master
.. requirement_status: https://requires.io/github/wkpalan/gaf-utils/requirements/?branch=master
