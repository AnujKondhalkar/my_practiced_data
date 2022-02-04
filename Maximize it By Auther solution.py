from itertools import *
'''
K, M = map(int, input().split())
N = []

for _ in range(K):
     N.append(list(int(x) for x in input().split()[1:]))
     #print(N)
MAX =0
for i in product(*N):
    print(i)
    MAX = max(sum(map(lambda x: x**2, i))%M, MAX)
    
print (MAX)
'''

'''
3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 
'''

K,M = map(int,input().split())
N = (list(map(int, input().split()))[1:] for _ in range(K))
#value = (map(lambda x: sum(i**2 for i in x)%M, product(*N)))
#print(max(value))
l=[]
for j in product(*N):
     l.append(sum(i**2 for i in j)%M)
print(l)
