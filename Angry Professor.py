def angryProfessor(k, a):
    # Write your code here
    count_early=0
    for time in a:
        if time<=0:
            count_early+=1
    if count_early<k:
        return 'YES'
    else:
        return 'NO'
#for i in range(t):
k=3
a=[-1,-3,4,2]
print(angryProfessor(k, a))
    
