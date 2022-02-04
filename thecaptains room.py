def thecaptainsroom(n ,c):
    # Write your code here
    c.sort()
    return (set(c[0::2])^set(c[1::2])).pop()





        
n = input()

c = list(map(int, input().rstrip().split()))

print(thecaptainsroom(n ,c))
