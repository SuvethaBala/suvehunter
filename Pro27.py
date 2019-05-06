n,W=map(int,input().split())
vt=list(map(int,input().split()))
val=list(map(int,input().split()))
ratio=[]
for i in range(n):
  ratio.append(val[i]/vt[i])
cost=0
while W>=0 and len(ratio)>0:
  if W>=vt[ratio.index(max(ratio))]:
    cost+=val[ratio.index(max(ratio))]
    W-=vt[ratio.index(max(ratio))]
  val.pop(ratio.index(max(ratio)))
  vt.pop(ratio.index(max(ratio)))
  ratio.pop(ratio.index(max(ratio)))
print(cost)
