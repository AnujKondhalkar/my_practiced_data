def utopianTree(n):
    # Write your code here   
    h=0
    for i in range(0,n+1):
        #print(i,'i')
        if i%2==0:
            h+=1
        else:
            h*=2
    return(h)

        



if __name__ == '__main__':
    print(utopianTree(0))
    print(utopianTree(1))
    print(utopianTree(2))
    print(utopianTree(3))
    print(utopianTree(4))
    print(utopianTree(5))
    print(utopianTree(6))
    print(utopianTree(7))
