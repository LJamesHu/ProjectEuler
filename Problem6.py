# Sum square difference
# Problem 6

# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385

# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 552 = 3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# Get limit
numOfNumbers = 100

# Set counters
sumOfSquares = 0
squareOfSum = 0

# Input numbers in
for n in range(1,numOfNumbers+1):
    sumOfSquares += n**2
    squareOfSum += n

# Get answer
print squareOfSum**2 - sumOfSquares