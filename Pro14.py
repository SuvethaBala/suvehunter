from operator import xor
from functools import reduce

nq = input().split()
n = int(nq[0])
q = int(nq[1])

in_nums = list(map(int, input().split()))

for _ in range(q):
    k, v = map(int, input().split())
    x = reduce(xor, in_nums[k-1:v])
    print(x)
