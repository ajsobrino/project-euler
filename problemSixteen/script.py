number=2**1000
i=0
sum=0
while number != 0 :
    sum+=number%10
    number=number//10
print(sum)