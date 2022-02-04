def findSum(numbers, queries):
    # Write your code here
    numbers=[0]+numbers
    a=numbers
    k=queries
    m=[]
    for q in k:
        q=q
        if 0 in a[q[0]:q[1]+1]:
            #print(a[q[0]:q[1]+1])
            m.append(sum(a[q[0]:q[1]+1])+q[-1])

        else:
            #print(a[q[0]:q[1]+1])
            m.append(sum(a[q[0]:q[1]+1]))
                
    return m







queries=[[1,2,5]]
numbers=[5,10,10]
print(findSum(numbers, queries))


queries=[[1,2,10],[2,2,20]]
numbers=[-5,0]
print(findSum(numbers, queries))


