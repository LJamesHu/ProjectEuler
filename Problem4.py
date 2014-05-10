# Largest palindrome product
# Problem 4

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

# Set up numbers
nmax = 999
nmin = 99
number = nmax*nmax

# Iterate numbers down from max number
numNotFound = True
while numNotFound:
    # Check if palindrome
    if number == int(str(number)[::-1]):
        # Get numbers below max number
        for num in range(nmax,nmin,-1):
            # Check if number is divisible by a n digit number, and that the result is a n digit number
            if number%num == 0 and len(str(number/num)) == len(str(nmax)):
                # Print results
                print number
                print num
                print number/num
                # Break out of loops
                numNotFound = False
                break
    # If neither, iterate down
    number -= 1