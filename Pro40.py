from itertools import permutations
li=list(permutations(['d','h','o','n','i']))
a=input()
n=[]
for i in li:
  if i not in n:
    n.append(''.join(i))
for i in n:
  if i==a:
    print('yes')
    break
else:
  print('no')
