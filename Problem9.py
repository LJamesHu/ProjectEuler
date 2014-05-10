# Special Pythagorean triplet
# Problem 9

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2

# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# Iterate through
for x in range (1, 500):
    for y in range (x + 1, 500):
            for z in range(y + 1, 500):
                # Check under conditions
                if x**2 + y**2 == z**2 and x+y+z == 1000:
                    # Print result
                    print x*y*z