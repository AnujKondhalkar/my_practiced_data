def thecaptainsroom(n ,c):
    # Write your code here
    c.sort()
    print((set(c[0::2])),'--',(set(c[1::2])))
    print(((c[0::2])),'--',((c[1::2])))


c=[1,2,3,6,5,4,4,2,5,3,6,1,6,5,3,2,4,1,2,5,1,4,3,6,8,4,3,1,5,6,2,9,9,9,9,9]
n=5
thecaptainsroom(n ,c)
