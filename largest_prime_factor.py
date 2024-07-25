import numpy as np

number = 600851475143
divisors = []
i = 1
for i in range(1,number+1):
  if ((number % i == 0) and (i != 0)):
    divisors.append(i)
    number = int(number/i)
    print("now the number is", number)
    if (number == 1):
      break

print("the list of divisors is: ")
print(divisors)
print("the largest prime factor is = ", np.max(divisors))