def binary(x):
   if x > 1:
       binary(x//2)
   print(x % 2,end = '')
dec = int(input())
binary(dec)
