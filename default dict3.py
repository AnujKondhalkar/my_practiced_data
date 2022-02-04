from collections import defaultdict

n,m = list(map(int,input().split()))
d = defaultdict(list)
for i in range(n):
    d[input()].append(i+1)
    print(d)
for i in range(m):
    print(*d[input()] or [-1])
