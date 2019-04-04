b=[]
for _ in range(int(input())):
    l=list(map(int,input().split()))
    for i in l:
        b.append(i)
b.sort()
print(*b)
