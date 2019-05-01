n,k=map(int,input().split())
l=list(map(int,input().split()))
p=[]
s=""
for i in range(0,len(l)):
    p.append([l[i],abs(l[i]-k)])
p.sort(key=lambda x:x[1])
if p[0][1]==0:
    p.remove(p[0])
for i in range(0,3):
    s=s+str(p[i][0])+" "
print(s.strip())
