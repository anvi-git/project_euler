#Problem #5
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#link to the problem: https://projecteuler.net/problem=5

def greatest_common_divisor(a, b): #this calculates the greatest commons divisor. Sets a equal to b, and b equal to a % b. 
                                   #This happens until b = 0. When this happens, a is the greatest commonos divisor of the original
                                   #a and b  
  while b:
    a, b = b, a % b
  return a

def least_common_multiple(a, b):
  return a * b // greatest_common_divisor(a, b)

def least_common_multiple_for_range(n):
  lcm = 1
  for i in range(1, n + 1):
    lcm = least_common_multiple(lcm, i)
  return lcm 

result = least_common_multiple_for_range(20)

print("the smallest positive number evenly divisible by all numbers from 1 to 20 is ", result)