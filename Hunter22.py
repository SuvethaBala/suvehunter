s=int(input())
l1=list(map(int,input().split()))
v=1
l=[]
for i in l1:
  v=v*i
for i in l1:
  l.append(v//i)
print(*l)
