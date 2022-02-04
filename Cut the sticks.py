def cutTheSticks(arr):
    # Write your code here
    b=arr
    c=[]
    count_stick=[]
    while len(b)!=0:
        #print(len(b),'len')
        count_stick.append(len(b))
        #print(len(b))
        for i in (b):
            #print(b)
            c.append(i-min(b))
        b=c
        for i in range(b.count(0)):
            b.remove(0)
        else:
            pass
        #b.remove(min(b))
        c=[]
        #print(b)
    return count_stick




           
arr1=[5,4,4,2,2,8]
arr2=[1,2,3,4,3,3,2,1]
arr3=[arr1,arr2]
for i in arr3:
    for i in (cutTheSticks(i)):
        print(i)
    print('ok')
        

