N=int(input())
dash=(N*2)-1
for i in range(N+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    a=str(((10**i)//9)**2)
    print(a.center(dash,'-'))
