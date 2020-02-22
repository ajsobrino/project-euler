
limit =1000
max=0
def all_combination():
    max =0
    for i in range(100,limit):
        for j in range(i,1000):
            x= i*j
            palimdromic = str(x)
            if is_palimdromic(palimdromic) and x > max:
                max = x
                print('The numbers are: '+str(i)+' and '+str(j))
    return max

def is_palimdromic(x):
    n = len(x)
    limit=int(n/2)
    result = True
    for i in range(limit):
        if   x[i]!=x[n-i-1]:
            result = False
    return result


if __name__ == '__main__':
    print(str(all_combination()))
