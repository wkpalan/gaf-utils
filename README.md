python-package-boilerplate
==========================

[![Build Status](https://api.travis-ci.org/wkpalan/gaf-utils.png?branch=master)](https://travis-ci.org/wkpalan/gaf-utils)
[![Requires.io](https://requires.io/github/mtchavez/python-package-boilerplate/requirements.svg?branch=master)](https://requires.io/github/mtchavez/python-package-boilerplate/requirements?branch=master)

Boilerplate for a Python Package

## Package

Basic structure of package is

```
├── README.md
├── packagename
│   ├── __init__.py
│   ├── packagename.py
│   └── version.py
├── pytest.ini
├── requirements.txt
└── setup.py
```

## Requirements

Package requirements are handled using pip. To install them do

```
pip install -r requirements.txt
```

## Travis CI

There is a ```.travis.yml``` file that is set up to run your tests for python 2.7
and python 3.2, should you choose to use it.
