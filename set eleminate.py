n = int(input())
s = set(map(int, input().split()))
N=int(input())
for i in range(N): 
    com=input().split()
    if com[0]=='pop':
        s.pop()
    elif com[0]=='remove':
        s.remove(int(com[1]))
    elif com[0]=='discard':
        s.discard(int(com[1]))
print(*s)


'''
n = int(input())
s = set(map(int, input().split())) 
for i in range(int(input())):
    eval('s.{0}({1})'.format(*input().split()+['']))

print(sum(s))

'''
