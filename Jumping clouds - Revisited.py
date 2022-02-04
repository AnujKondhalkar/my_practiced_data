def jumpingOnClouds(c, k):
    # Write your code here
    n=len(c)
    i=0
    s=0
    energy=100
    #c=[0,0,1,0,0,1,1,0]
    #l=[0,1,2,3,4,5,6,7]

    while energy!=0:
        #print(energy,'e')
        i+=k
        m=(i)%n
        #print(m,'M')
        #print(l[m],'value position')
        if c[m]==0 :
            
            energy-=1
            if m==0:
                break
            
        elif c[m]==1:
            
            energy-=3
            if m==0:
                break
            
    return energy

'''
k=2
c=[0,0,1,0,0,1,1,0]
print(jumpingOnClouds(c, k))
'''

k=3
c=[1 ,1 ,1 ,0 ,1 ,1 ,0 ,0 ,0 ,0]
print(jumpingOnClouds(c, k))

