n = int(input())
in_nums = list(map(int, input().split()))

no_of_ones = []
for j in in_nums:
    count = 0
    while j:
        j &= (j-1)
        count += 1
    no_of_ones.append(count)

result = sorted(zip(no_of_ones, in_nums), reverse=True)
