import math

for i in range(1,998):
    for j in range(i,998):
        tern = i*i+j*j
        k= int(math.sqrt(tern))
        if tern == (k*k) :
            if (i+j+k) == 1000 :
                print('i is '+str(i)+ ' and j is '+str(j))
                print(str(i*k*j))