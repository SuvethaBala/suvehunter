y, a, f, k = map(int, input().split())
count = 0
a1 = a-f
if (a1 >= 0):
    di = (y-f)*2
    for i in range (k):
        if (i == k-1):
             di =di/ 2
        if (a1 < di):
            a1 = a
            count += 1
        a1 = a1 - di
        if (a1 < 0):
            count = -1
            break
        di = 2*y - di

    print (count)
else:
    print (-1)
