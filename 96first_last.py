def firstDigit(x) : 
  while x >= 10:
    x = x / 10;
  return int(x) 
def lastDigit(x) : 
  return (x % 10) 
x = int(input()) 
print(firstDigit(x)+lastDigit(x), end = " ") 
