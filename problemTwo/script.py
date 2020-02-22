x_n_1=1
x_n=1
aux=0
sum=0
while x_n<4000000 :
    if x_n%2==0:
        sum+=x_n
    aux =x_n
    x_n+=x_n_1
    x_n_1=aux
print(sum)