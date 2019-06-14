n,p,q,r=map(int,input().split())
m=list(map(int,input().split()))
c=[]
for i in range(0,len(m)):#loopstarts
	for j in range(i,len(m)):
		for k in range(j,len(m)):
			c.append(p*m[i]+q*m[j]+r*m[k])#loopends
print(max(c))
