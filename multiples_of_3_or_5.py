#Problem 1
#If we list all the natural numbers below 10
#that are multiples 3 of or 5, we get 3, 5, 6, and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
# link to the problem https://projecteuler.net/problem=1

import math

sum = 0 #this stores the sum of the desired numbers
i = 0 #this counts up to 1000

while (i <= 1000):
  if (i%3 == 0) or (i%5 == 0):
    sum += i 
  i += 1
    
print(sum)
