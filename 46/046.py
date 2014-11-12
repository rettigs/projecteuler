#!/usr/bin/env python
"""
Project Euler Problem 46
========================

It was proposed by Christian Goldbach that every odd composite number can
be written as the sum of a prime and twice a square.

9 = 7 + 2 * 1^2
15 = 7 + 2 * 2^2
21 = 3 + 2 * 3^2
25 = 7 + 2 * 3^2
27 = 19 + 2 * 2^2
33 = 31 + 2 * 1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a
prime and twice a square?
"""

def primes():
    n = 1
    while True:
        n += 1
        prime = True
        for i in xrange(2, n//2):
            if n % i == 0:
                break
        yield n

for p in primes():
    print p

testnum = 33
#while True
#    testnum += 2


