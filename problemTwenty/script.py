number=1
for i in range(2,101):
	number *=i
i=0
sum=0
while number != 0 :
    sum+=number%10
    number=number//10
print(sum)
