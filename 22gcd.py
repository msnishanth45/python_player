x,y = list(map(int,input().strip().split()))[:2] 
i=1
while(i <= x and i <= y):
    if(x % i == 0 and y % i == 0):
        gcd = i
    i = i + 1
print(gcd)
