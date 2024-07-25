#Problem 4
#A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
#Find the largest palindrome made from the product of two 3-digit numbers.
#link to the problem: https://projecteuler.net/problem=4
import numpy as np 

number = []
palindrome = []
for i in range(100, 1000):
  for j in range(100, 1000):
    number = i*j
    number_string = str(number)
    if (number_string[0] == number_string[-1]):
      if (number_string[1] == number_string[-2]):
        if (number_string[2] == number_string[-3]):
          palindrome.append(number)

print(np.max(palindrome))
