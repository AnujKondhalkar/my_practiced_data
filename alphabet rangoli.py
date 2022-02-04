def print_rangoli(size):
    # your code goes here
    N=size
    st=''
    l2=[]
    l3=[]
    for i in range(1,N+1):
        st=''
        for j in range (i):
            st=st+str((((chr(96+N-j)))))
        l2.append(st)
    for i in range(0,len(l2)):
            l3.append(l2[i]+l2[i][::-1][1::])
    L=(len(l3[-1])*2)-1
    for i in range(len(l3)):
        print('-'.join(l3[i]).center(L,'-'))
    for i in range(len(l3)-2,-1,-1):
        print('-'.join(l3[i]).center(L,'-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(17)


'''
#hackerrank
n = int(input())
for i in range(n):
    s = "-".join(chr(ord('a')+n-j-1) for j in range(i+1))
    print((s+s[::-1][1:]).center(n*4-3, '-'))

for i in range(n-1):
    s = "-".join(chr(ord('a')+n-j-1) for j in range(n-i-1))
    print((s+s[::-1][1:]).center(n*4-3, '-'))

#['e', 'ed', 'edc', 'edcb', 'edcba']
'''




    
'''
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
[::-1]
'''
