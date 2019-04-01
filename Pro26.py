n=int(input())
k=input().split()
s=0
l=[]
for i in range(0,len(k)-1):
	if int(k[i+1])>=int(k[i]):
		s=s+1
	else:
		l.append(s)
		s=0
print(max(l)+1)
