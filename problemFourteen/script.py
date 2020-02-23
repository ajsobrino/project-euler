
def calculate_next_number(n):
    if n%2 == 0:
        return n//2
    else :
        return (3*n+1)

def calculate_long_chain(n):
    following = True
    i=1
    x_n = n
    while following:
        x_n = calculate_next_number(x_n) 
        i+=1
        if  x_n == 1:
            break
    return i

def calculate_maximum_long_chain():
    maxChain=0
    max=0
    for i in range(1,1000000):
        longChain = calculate_long_chain(i)
        if longChain > maxChain :
            maxChain = longChain
            print(i)
            max = i
    return max

if __name__ == '__main__' :
    print(calculate_maximum_long_chain())
