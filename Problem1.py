# Multiples of 3 and 5
# Problem 1

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.


# Get the number to check below
below = 1000
# Calculation for total
total = 0

# Make more generalized by using variables
f1 = 3
f2 = 5

# Quick Iteration
# Relatively inefficient, but very quick

# Check to the range indicated
for i in range(0, below):
	# If it is a multiple of 5 or 3
	if i % f1 == 0 or i % f2 == 0:
		# Iterate total to add that number
		total += i

print total

# Arithmetic Sums
# Very efficient code, useful for large numbers

# Calculation for total
total = 0

# Find sum of factor 1, (first term + #terms*factor)(#terms/2)
sumf1 = (f1 + (((below-1)/f1))*f1) * ((below-1)/f1)/2
# Find sum of factor 2, (first term + #terms*factor)(#terms/2)
sumf2 = (f2 + (((below-1)/f2))*f2) * ((below-1)/f2)/2
# Find sums of shared terms between factor 1 and 2, (first term + #terms*factor)(#terms/2)
sumf1f2 = (f1*f2 + (((below-1)/(f1*f2)))*(f1*f2)) * ((below-1)/(f1*f2))/2

# Sum them up
total = sumf1 + sumf2 - sumf1f2

print total