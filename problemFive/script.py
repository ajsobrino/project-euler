j=19
theEnd= False
while not theEnd : 
    j=j+1
    for i in range(1,21):
        if j%i != 0 : 
            theEnd = False
            break
        theEnd = True
    print(j)