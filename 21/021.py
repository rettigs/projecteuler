#!/usr/bin/env python
"""
Project Euler Problem 21
========================

Let d(n) be defined as the sum of proper divisors of n (numbers less than
n which divide evenly into n).
If d(a) = b and d(b) = a, where a =/= b, then a and b are an amicable pair
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22,
44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1,
2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from __future__ import division

SUMFOR = 10000

divisorTable = {}
for i in xrange(1, SUMFOR):
    divisors = []
    for j in xrange(1, i//2+1):
        if i % j == 0:
            divisors.append(j)
    divisorTable[i] = sum(divisors)

amicableNumbers = set()
for n, s in divisorTable.iteritems():
    if s in divisorTable and divisorTable[s] == n and s != n:
        amicableNumbers.add(n)

print sum(amicableNumbers)
