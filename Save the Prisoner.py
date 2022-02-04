# n:the number of prisoners
# m:the number of sweets
# s:the chair number to start passing ot treats at

def saveThePrisoner(n, m, s):
    # Write your code here
    return (s-1 + m-1)%n +1


'''

t=int(input())
while(t>0):
    n,m,s=map(int,input().split())
    p=s+m-1
    while(p>n):
        p=p-n
    print(p)
    t=t-1
    
'''




n=7;m=19;s=2
ans=6
print(saveThePrisoner(n, m, s))
n=3;m=7;s=3
ans=3
print(saveThePrisoner(n, m, s))
n=5;m=2;s=1
ans=2
print(saveThePrisoner(n, m, s))
n=5;m=2;s=2
ans=3
print(saveThePrisoner(n, m, s))
'''
for t in range(100):
    p = input().split()
    saveThePrisoner(int(p[0]), int(p[1]), int(p[2]))
# n:the number of prisoners
# m:the number of sweets
# s:the chair number to start passing ot treats at


T = int(input())
for i in range(T):
    N,M,S = list(map(int, input().split()))
    res = (S+M-1)%N
    if res is 0:
        res = N
    print(res)


'''
