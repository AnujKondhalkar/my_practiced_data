# Enter your code here. Read input from STDIN. Print output to STDOUT 
from itertools import combinations
value=int(input())
count=0
lst=list(combinations(sorted(input().split(' ')),int(input())))
for i in lst:
    if 'a' in i:
        count=count+1 
print(lst)
print(len(lst))
print("%.12f" % (count/len(lst)))
