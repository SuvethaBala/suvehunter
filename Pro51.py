def check(l):
	c=1
	for i in range(0,len(l)-1):
		if l[i]!=l[i+1]:
			c=c+1
		else:
			break
	return c
n=int(input())
l=list(map(int,input().split()))
for i in range(0,len(l)):
	if l[i]>0:
		l[i]=1
	else:
		l[i]=0
v=""		
for i in range(0,len(l)):
	k=l[i::]
	=v+str(check(k))+" "
print(v.strip())
