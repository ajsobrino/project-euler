import math
factorPrime = []
x = 600851475143
limitLoop = int(math.sqrt(x))+1

for i in range(3,limitLoop,2):
    if x%i==0:
        x = x/i
        while x%i==0:
            x=x/i
        factorPrime.append(i)
print(factorPrime)

