def sockMerchant(n, ar):
    # Write your code here
    l={}
    count=0
    for i in ar:
        if i not in l:
            l[i]=ar.count(i)
            #print(l)
    for i in l.values():        
        count+=(i-i%2)//2
    return count



n=7
ar=[1,2,1,2,1,3,2]
print(sockMerchant(n, ar))



n=3
ar=[10,20,30]
print(sockMerchant(n, ar))
