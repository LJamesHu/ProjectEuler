# Summation of primes
# Problem 10

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

import math

# Set starting prime number
pnum = 3

# Skip first prime so can iterate by 2
sumOfPrimes = 2


# Iterate prime numbers while still less than number
while pnum < 2000000:
    # Check if prime
    if all(pnum%i!=0 for i in range(2,int(math.sqrt(pnum))+1)):
        sumOfPrimes += pnum
    # Iterate by 2 to skip even numbers
    pnum += 2

# Largest prime factor
print sumOfPrimes