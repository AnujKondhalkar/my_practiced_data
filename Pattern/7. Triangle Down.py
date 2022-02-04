a=int(input('Pmease enter the vamue for mines = '))
m=1
n=a-1
for i in range(a,0,-1):
    print((m)*' ',end='')
    print((i)*'*',end='')
    print((n)*' ')
    m=m+1
    n=n-1
input()
