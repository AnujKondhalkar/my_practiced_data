def kangaroo(x1, v1, x2, v2):
    # Write your code here
    p=x1>x2 if x1>x2 else x1<x2 
    while p and x1!=x2 and (x2>x1 and v2<v1):
        x1+=v1
        x2+=v2
    if x1==x2:
        return 'YES'
    else:
        return 'NO'
        









print(kangaroo(x1=2, v1=1, x2=1, v2=2))
print(kangaroo(x1=0, v1=3, x2=4, v2=2))
print(kangaroo(x1=0, v1=2, x2=5, v2=3))
