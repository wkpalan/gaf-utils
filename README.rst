go_utils
=========

This is a simple python utility to read and write Gene Ontology related Files (e.g. gaf, obo).
Will be updated to do more complicated filtering later on

Build Status |buildstatus| Requirement Status |requirementstatus|


## Package
Basic structure of package is
::

    ├── README.rst
    ├── utils
    │   ├── __init__.py
    │   ├── gaf.py
    │   └── obo.py
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

.. |buildstatus| image:: https://travis-ci.org/wkpalan/go_utils.svg?branch=master
  :target: https://travis-ci.org/wkpalan/go_utils

.. |requirementstatus| image:: https://requires.io/github/wkpalan/go_utils/requirements.svg?branch=master
  :target: https://requires.io/github/wkpalan/go_utils/requirements/?branch=master
