#Problem #6
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
#link to the problem: https://projecteuler.net/problem=6

sum_squares = 0 #this is the variable that will store the sum of the squared numbers ranging from 1 to 100
sum = 0 #this is the variable that will store the sum of those same numbers
difference = 0 #this is the variable that will store the difference between "sum_squares" and the square of "sum"

for i in range(1,101):
  #print("i = ", i)
  term = i*i
  #print("term", term)
  sum_squares += term
  #print("sum_squares = ", sum_squares)
  sum += i
  
#print(sum_squares)
difference = sum_squares - sum*sum
print("the difference between the sum of the squares ", sum_squares, " and the square of the sum ", sum, " is = ", difference)