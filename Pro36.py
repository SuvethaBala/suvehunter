import sys,string
num = int(input())
L = [ int(x) for x in input().split()]
num = len(L)
cnt = 0
for i in range(0,num-2) :
    for j in range(i+1, num-1):
        for k in range(j+1, num):
            if L[i] > L[j] > L[k] :
                cnt += 1
print(cnt)
