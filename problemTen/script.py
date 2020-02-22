import math

total=2
j=1
prime = True
while j<=2000000:
	j+=2
	limit =int(math.sqrt(j))+1
	for  k in range(3,limit,2):
		if j%k == 0:
			prime = False
			break
	if prime:
		total+=j
	prime = True
print(total)
