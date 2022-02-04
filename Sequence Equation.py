def permutationEquation(p):
    # Write your code here
    new_=[]
    for i in range(1,len(p)+1):
        j=(p.index(i)+1)
        #print(j,'j')
        k=p.index(j)+1
        new_.append(k)#,'k')
    return new_
        
        






p=[4, 3, 5, 1, 2]
print(permutationEquation(p))
