m,n=map(int,input().split())
v=list(map(int,input().split()))[:m]
if n in v:
  print(n)
else:
  print(n-1)
