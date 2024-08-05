#Problem #9 - Project Euler
#There exists exactly one Pythagorean triplet for which a + b + c = 1000
#Find the product abc
#link to the problem: https://projecteuler.net/problem=9
a = 0
b = 0
c = 0
sum = 1000

for a in range(0, int(sum/2)):
  for b in range(a+1, int(sum/2)):
    c = int((a*a + b*b)**0.5)
    if (int(a) + int(b) + c == sum):
      if (int(a)*int(a) + int(b)*int(b) - int(c)*int(c) == 0):
        print("the pythagoream triple is a = ", a, "; b = ", b, "; c = ", c)
  
print("the product of abc is = ", a*b*c)
