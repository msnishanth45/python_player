mm,nn = list(map(int,input().strip().split()))[:2] 
sum=0
for i in range(mm,nn+1):
    if i%2!=0:
       sum=sum+i
print(sum)
