# fermat

> A collection of efficient number theoretic algorithms and data structures

[![Build Status](https://travis-ci.com/horeilly1101/fermat.svg?branch=master)](https://travis-ci.com/horeilly1101/fermat)
[![codecov](https://codecov.io/gh/horeilly1101/fermat/branch/master/graph/badge.svg)](https://codecov.io/gh/horeilly1101/fermat)

## Description

Fermat contains algorithms and data structures to efficiently
compute many important results in number theory. Most methods are
based off of `MATH 365` at Rice University and *A Friendly
Introduction to Number Theory* by Joseph H. Silverman.

### This library includes:

- Arithmetic functions and the dirichlet convolution
- Continued fractions
- Cryptographic operations and the RSA algorithm
- Efficient algorithms to solve common diophantine equations
    - Linear, Sum of Squares, Pell-like, etc.
- Common factorization strategies
- Primality testing (Rabin-Miller)
- Operations with quadratic reciprocity and the Jacobi symbol
- Random (large) prime generation
- An algorithm to compute modular inverses
- Various utility methods
- And more to come ...

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
large public/private keys for RSA encryption. You can run the server
with
```
python3 run_server.py
```

The server will then be available at `localhost:2345`. The only
available `GET` endpoint is `/get-keys/<min_bits>`, where `min_bits`
is an integer that specifies the minimum allowable bits in the
public key. The private key and modulus will have about twice
as many bits.

### Example Response

    {
        min_bits: 10,
        publicKey: "0x3d981",
        privateKey: "0x568bcc181",
        modulus: "0xdab06fce1"
    }

## How to test

Tests are set up with the `unittest` module. You can run them with
```
python3 -m unittest
```
