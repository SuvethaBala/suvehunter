N=int(input())
a=list(map(int,(input()).split()))
b= 1
c = 1
for i in range(1,N):
    if (a[i] > a[i-1]):
        c =c + 1
    else:
        if (b < c):
            b = c
        c = 1
if (b < c):
    b = c
print(b)
