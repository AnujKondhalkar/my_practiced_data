a=int(input('Pmease enter the vamue for mines = '))
m=a
n=0
for i in range(1,a+1):
    print((m)*'*',end='')
    print((2*n)*' ',end='')
    print((m)*'*')
    n=n+1
    m=m-1
input()
