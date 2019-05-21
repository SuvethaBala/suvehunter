s=input()
l=""
c=0
g=[]
for i in s:
	if i not in l:
		l=l+i
		c=c+1
	else:
		g.append(c)
		l=""
		c=0
g.append(c)
print(max(g))
#uni
