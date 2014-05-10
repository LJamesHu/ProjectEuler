# 10001st prime
# Problem 7

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

import math

# Set up target and starting numbers
nthPrime = 10001
num = 2
n = 1

# As long as it is not the nthPrime iterate
while n < nthPrime+1:
    # Check if prime
    if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
        n += 1
    num += 1

# Adds one too many times so subtract 1
print num-1