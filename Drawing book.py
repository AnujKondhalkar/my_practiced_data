def pageCount(n, p):
    # Write your code here
    turns=[]
    if n%2==0:
        n+=1
    if p==1:
        return 0
    count=0
    for i in range(0,n,2):
        #print(count,'---','page turn.')
        #print(i,'----',i+1)
        if i==p or i+1==p:
            #print(count)
            turns.append(count)
            break
        count+=1

    count=0
    #print('loop 2')
    for i in range(n,0,-2):
        #print(count,'---','page turn.')
        #print(i,'----',i-1)
        if i==p or i-1==p:
            #print(count)
            turns.append(count)
            break
        count+=1

    return min(turns)



'''
def pageCount(n, p):
    if not n%2:
        n += 1
    return min(p//2, (n-p)//2)

'''
        
        


n=5
p=4
(pageCount(n, p))


n=6
p=2
(pageCount(n, p))
