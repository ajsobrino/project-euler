limit = 100

sumSquare = 0
SquareSum = 0

sumSquare = sum( list(range(1,101)))**2
SquareSum = sum( i*i for i in range(101))

print(str(sumSquare-SquareSum))