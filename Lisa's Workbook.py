def workbook(n, k, arr):
    # Write your code here
    l=[]
    a=[]
    count=0
    for i in arr:
        for j in range(1,i+1):
            a.append(j) 
        for i in range(0,len(a),k):   
                l.append(a[i:i+k:])
                if len(l) in a[i:i+k:]:
                    count+=1
        a=[]
    return count

n=5;k=3
arr=[4,2,6,1,10]
print(workbook(n, k, arr))



'''

def workbook(n, k, arr):
    # Write your code here
    l=[]
    a=[]
    count=0
'''
#example
'''
    #n=5
    #k=3
    #arr=[4,2,6,1,10]
    for i in arr:
        for j in range(1,i+1):
            a.append(j) 
        for i in range(0,len(a),k):   #k=3
                l.append(a[i:i+k:])
                #print(a[i:i+k:])
                #print(len(l),'len of l')
                if len(l) in a[i:i+k:]:
                    count+=1
        a=[]
    return count

n=5;k=3
arr=[4,2,6,1,10]
print(workbook(n, k, arr))

'''
