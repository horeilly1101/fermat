# numbers

> A collection of efficient number theoretic algorithms and data structures

[![Build Status](https://travis-ci.com/horeilly1101/fermat.svg?branch=master)](https://travis-ci.com/horeilly1101/fermat)
[![codecov](https://codecov.io/gh/horeilly1101/fermat/branch/master/graph/badge.svg)](https://codecov.io/gh/horeilly1101/fermat)

## How to run

Set up the environment and install dependencies.
```
# start in the repository directory
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

Run the server.
```
python3 run_server.py
```

The server will then be available at `localhost:2345`.

## How to test

Tests are set up with the `unittest` module. You can run them with
```
python3 -m unittest
```
