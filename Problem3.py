# Largest prime factor
# Problem 3

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import math

# Set up number
number = 600851475143

# Set starting prime number
pnum = 2

# Iterate prime numbers while still less than number
while pnum < number:
    # Check if prime
    if all(pnum%i!=0 for i in range(2,int(math.sqrt(pnum))+1)):
        # While still divisible, divide number by prime number
        while number%pnum == 0:
            number = number/pnum
    # Iterate
    pnum += 1

# Largest prime factor
print number