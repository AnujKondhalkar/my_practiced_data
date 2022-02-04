def circularArrayRotation(a, k, queries):
    # Write your code here
    rotation=k%len(a)
    l=len(a)
    q=len(queries)
    for i in range(q):
        position=(queries[i]-k+l)%l
        queries[i]=a[position]
    return queries
     






a=[3,4,5]
k=2
queries=[1,2]
print(circularArrayRotation(a, k, queries))

'''
answer will be:-

[3,4,5]
[5,3,4]
[4,5,3]


def circularArrayRotation(a, k, queries):
    # Write your code here
    for times in range(k):
        a=a[len(a)-1::]+a[:len(a)-1:]
    for ele in queries:
        return [a[ele] for ele in queries]



'''
