import sys


#n,m = input().strip().split(' ')
#n,m = [int(n),int(m)]
#c = [int(c_temp) for c_temp in input().strip().split(' ')]

def flatlandSpaceStations(n, c):
    c.sort()
    print((c[1:], c),' c[1:], c')
    maxgap = max(a-b for a, b in zip(c[1:], c)) if len(c) > 1 else 0
    #print(maxgap//2, c[0], n-1-c[-1])
    ans = max(maxgap//2, c[0], n-1-c[-1])
    return(ans)



n=5   # Number of cities
      # m=2
m = 2
c=[0,4] # c[m] Cities have station indices of a city with space station
      # m = 2 ... [0,4] c[0] c[1] c[2] c[3] c[4]
      # only 0 and 4 have the space station
print(flatlandSpaceStations(n, c))
