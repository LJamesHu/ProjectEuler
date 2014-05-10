# Smallest multiple
# Problem 5

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Setup problem
hiNum = 20
num = 1
n = 1

# Brute force code

while n < hiNum+1:
    # Must be a multiple of the highest number so reduced steps this way
    # Check against all values less than highest number
    if (num*hiNum)%n != 0:
        # If not, reset and start over
        n = 1
        num += 1
    # Iterate it if does pass
    n += 1

# Show results
print num*hiNum

# Alternate, but much more efficient code, running into problems with duplicate factors mucking up the calculation.

# while hiNum > 1:
#     print num%hiNum
#     if num%hiNum != 0:
#         num = num*hiNum
#         print "Number here"
#         print num
#     hiNum -= 1
# print num