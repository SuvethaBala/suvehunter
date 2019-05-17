a=input()
flag=0
for i in range(0,len(a)-1):
  for j in range(i+1,len(a)):
    if a[i]<a[j]:
      flag=1
      print(a[j:])
      break
  if flag==1:
    break
else:
  print(a)
