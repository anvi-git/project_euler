#Problem#10 - Project Euler
#Find the sum of all primes below two million.
#link to the problem: https://projecteuler.net/problem=10

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
sum = 0
for j in range (2,2000001):
  if is_prime(j) == True:
    sum += j
 
print(sum)