def pickingNumbers(a):
    # Write your code here
    i=0
    j=0
    lm=[]
    ln=[]
    a=sorted(a)
    while i!=len(a) and j!=len(a):
        if abs(a[i]-a[j])<=1:
            ln.append(a[j])
            j+=1
            print(ln)
            if ln not in lm:
                lm.append(ln)
        elif abs(a[i]-a[j])>1:
            ln=[]
            i=j
        print(lm)
    ln_len=0
    for i in lm:
        if len(i)>ln_len:
            ln_len=len(i)
    return(ln_len)

'''                        
a=[1,1,2,2,4,4,5,5,5]
print(pickingNumbers(a))
'''
a=[4,6,5,3,3,1]
print(pickingNumbers(a))
