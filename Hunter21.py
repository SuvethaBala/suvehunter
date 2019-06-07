n1,m=map(int,input().split())
a=[]
x=[]
for i in range(n1):
    a.append(list(map(int,input().split())))
for i in range(n1):
    for j in range(m):
        if a[i][j]==0:
            x.append(i)
            x.append(j)
for i in range(0,len(x),2):
    for h in range(m):
        a[x[i]][h]=0
    for h in range(n1):
        a[h][b[i+1]]=0
for i in range(n1):
    print(*a[i])
