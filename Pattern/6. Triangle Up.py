a=int(input('Pmease enter the vamue for mines = '))
m=a-1
n=1
for i in range(1,a+1):
    print((m)*' ',end='')
    print((n)*'*',end='')
    print((i-1)*'*')
    m=m-1
    n=n+1
input()
