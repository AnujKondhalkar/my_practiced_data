def equalizeArray(arr):
    # Write your code here
    #count=0
    l_c=[arr.count(i) for i in arr ]
    return len(arr)-max(l_c)
'''    print(l_c)
    j=max(l_c)
    for i in arr:
        if arr.count(i)!=j:
            count+=1
    return count'''


n=5
arr=[3,3,2,1,3]
print(equalizeArray(arr))
ans=2


n=6
arr=[37,32,97,35,76,62]
print(equalizeArray(arr))
ans=1




'''

from collections import Counter
def equalizeArray(arr):
    print(Counter(arr).values())
    return len(arr) - max(Counter(arr).values())

'''


n=43
arr=[35,65,69,28,12,69,37,80,80,50,80,50
     ,15,57,79,69,57,65,15,69,57,50,65
     ,2,14,64,15,65,65,5,15,64,57,37,
     50,12,64,37,28,20,80,80,50]

print(equalizeArray(arr))
ans=38



n=27
arr=[10,27,9,10,100,38,30,32,45,29,27,29,32,38,32,38,14,38,29,30,63,29,63,91,54,10,63]
print(equalizeArray(arr))
ans=23
