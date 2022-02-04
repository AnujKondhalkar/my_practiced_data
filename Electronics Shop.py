def getMoneySpent(keyboards, drives, b):
    # Write your code here.
    l=[]
    keyboards=sorted(keyboards)
    drives=sorted(drives)
    #print(keyboards,drives)
    for i in keyboards:
        for j in drives:
            if i+j>b:
                l.append(-1)
                break
            else:
                l.append(i+j)        
    return (max(l))







b=60
keyboards=[40,50,60]
drives=[5,8,12]
print(getMoneySpent(keyboards, drives, b))

b=5
keyboards=[4]
drives=[5]
print(getMoneySpent(keyboards, drives, b))
