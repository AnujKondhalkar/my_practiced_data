def flatlandSpaceStations(n, c):
    # Write your code here
    c.sort()
    result=0

    chain_len = c[0]-0    
    result=max(result, chain_len)

    for i in range(len(c)-1):
        chain_len = c[i+1] - c[i] -1
        if chain_len%2 == 0:
            mid = chain_len // 2
        else:
            mid = (chain_len+1)//2
        result = max(result, mid)

    chain_len = (n-1) - c[-1]
    return max(result, chain_len)

    
    



'''
def flatlandSpaceStations(n, c):
    # Write your code here
    # c=[0,4]
    l=set()
    p=set()
    mxl=len(c)
    if n == mxl:
        return 0
    for i in range (n):
        if i not in c:
            for j in c:
                print(j,'-- j  ',i,'-- i  ')
                p.add(abs(j-i))
                print(p)
            l.add(min(p))
            p=set()
    return max(l)

'''
'''
nm = input().split()

n = int(nm[0])

m = int(nm[1])

c = list(map(int, input().rstrip().split()))


print(flatlandSpaceStations(n, c))

'''
n=5   # Number of cities
      # m=2
m = 2
c=[0,4] # c[m] Cities have station indices of a city with space station
      # m = 2 ... [0,4] c[0] c[1] c[2] c[3] c[4]
      # only 0 and 4 have the space station
print(flatlandSpaceStations(n, c))
print('ok')
'''
n=3   
c=[1]
m=1
print(flatlandSpaceStations(n, c))

#c  =  [0 , 1 , 2 , 3 , 4 ]
#       0   1   3   4   5
'''
