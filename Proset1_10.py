n=int(input())
steps=(list(map(int.input().split))
sum=0
for i in range(l,len(steps)):
for j in range(0,i):
if (steps[j]< steps[i]):

sum=sum+steps[j]
print(sum)
