def super_reduce_st(st):
    for i in range(len(st)-1):
        print(i)
        i=0
        if st[i]==st[i+1]:
            st=st[:i]+st[i+1:]
            i=i+1
            print(i)
        else:
            i=i+1            
        return st
    else:
        st = 'Empty String'
    return st



    
    
st='abaaababba'
result=super_reduce_st(st)
print(result)


'''

>>> a='abaacedff'
>>> a[:2]+a[4:]


'''
