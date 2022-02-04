def getTotalX(a, b):
    count = 0
    for num in range(a[len(a)-1], b[0] + 1):
        v1 = all([num % numA == 0 for numA in a])
        print(left)
        v2 = all([numB % num == 0 for numB in b])
        print(right)
        count += v1*v2
    return count

a=[2,4]
b=[16,32,96]
print(getTotalX(a, b))





'''

def fact(i, a, b):
    for aa in a:
        if i % aa != 0:
            return False
    for bb in b:
        if bb % i != 0:
            return False
    return True

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
b = [int(b_temp) for b_temp in input().strip().split(' ')]

s = 0
for x in range(1, 101):
    if fact(x, a, b):
        s += 1
print(s)        

'''
