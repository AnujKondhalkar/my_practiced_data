n = int(input())
A = set(map(int, input().split()))
N=int(input())
for i in range(N): 
    com=input().split()
    if com[0]=='intersection_update':
        l = int(com[1])
        in_set= set(map(int, input().split()))
        A.intersection_update(in_set)
    elif com[0]=='update':
        l = int(com[1])
        in_set= set(map(int, input().split()))
        A.update(in_set)
    elif com[0]=='symmetric_difference_update':
        l = int(com[1])
        in_set= set(map(int, input().split()))
        A.symmetric_difference_update(in_set)
    elif com[0]=='difference_update':
        l = int(com[1])
        in_set= set(map(int, input().split()))
        A.difference_update(in_set)
print(sum(A))
