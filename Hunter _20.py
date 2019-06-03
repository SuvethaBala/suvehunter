def count1s(n):
  x=0
  while n!=0:
    if n%2==1:
      x+=1
    n=n//2
  return x
def isprime(n):
  
  if n>1:
    if n==2:
      return True
    else:
      for i in range(2,n):
        if n%i==0:
          return False
          break;
      else:
        return True

a,b=map(int,input().split())
counter=0
for i in range(a,b+1):
  if isprime(count1s(i)):
    counter+=1
print(counter)
