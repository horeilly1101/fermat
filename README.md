# fermat

> A collection of efficient number theoretic algorithms and data structures

[![Build Status](https://travis-ci.com/horeilly1101/fermat.svg?branch=master)](https://travis-ci.com/horeilly1101/fermat)
[![codecov](https://codecov.io/gh/horeilly1101/fermat/branch/master/graph/badge.svg)](https://codecov.io/gh/horeilly1101/fermat)

## Description

Fermat contains algorithms and data structures to efficiently
compute many import results in number theory. Most methods are
based off of `MATH 365` at Rice University and **A Friendly
Introduction to Number Theory** by Joseph H. Silverman.

### This library includes:

- arithmetic functions and the dirichlet convolution
- continued fractions
- cryptographic operations and the RSA algorithm
- efficient algorithms to solve common diophantine equations
    - Linear, Sum of Squares, Pell-like, etc.
- common factorization strategies
- primality testing (Rabin-Miller)
- operations with quadratic reciprocity and the Jacobi symbol
- random (large) prime generation
- an algorithm to compute modular inverses
- various utility methods
- and more to come ...

## How to use

Set up the environment and install dependencies.
```
# start in the repository directory
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

All code is available in the `/fermat` directory.

## RSA Encryption API

This project also contains a REST API that generates arbitrarily
public/private keys for RSA encryption. You can run the server
with
```
python3 run_server.py
```

The server will then be available at `localhost:2345`. The only
available endpoint is `/get-keys/<min_bits>`, where `min_bits`
is an integer that specifies the minimum allowable bits in the
public key. The public key and modulus will have about twice
as many bits.

### Example Response

    {
        
    }

## How to test

Tests are set up with the `unittest` module. You can run them with
```
python3 -m unittest
```
