import sys,string
num = int(input())
M = [ int(x) for x in input().split()]
num = len(M)
if num==1 :
    print(1)
    sys.exit()
cnt = 0
for i in range(1,num-1) :
    if ((M[i] > M[i-1]) and (M[i] > M[i+1])) or ((M[i] < M[i-1]) and (M[i] < M[i+1])):
        cnt += 1
print(cnt)
