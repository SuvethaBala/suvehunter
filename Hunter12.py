n,k=map(int,input().split())
l=[int(x) for x in input().split()]
l=sorted(l)
x=l[::-1]
print(x[k-1])
