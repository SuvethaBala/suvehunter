num,k=map(int,input().split())
b=list(map(int,input().split()))
if k==1:
  print(min(b))
elif k==2:
  m=b[0]
  temp=b[0]
  for i in range(1,num-1):
    if min(b[:i])>min(b[i+1:]):
      temp=min(b[:i])
    else:
      temp=min(n[i+1:])
    if temp>m:
      m=temp
  print(m)
else:
  print(max(b))
