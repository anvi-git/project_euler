import math

i = 0
sum = 0

old_fib = 0
new_fib = 1
fib = 0
while (fib <= 4000000):
  print("old fib = ", old_fib)
  print("new fib = ", new_fib)
  fib = new_fib + old_fib
  print("fib number = ", fib)
  print(" - - - - ")
  old_fib = new_fib
  new_fib = fib
  i += 1
  if ((fib %2 == 1) and (fib <= 4000000)):
    sum += fib
    print("the sum here is = ", sum)
    print(" - - - - ")
print("the sum is", sum)