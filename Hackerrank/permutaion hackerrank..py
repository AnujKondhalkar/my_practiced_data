''''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations,combinations
in1=input().split(' ')
print('Permutations for ',str(in1[0]))
a=list(permutations(sorted(in1[0]),int(in1[1])))
for i in a:
	print(''.join(list(i)).upper())

print('Combinations for ',str(in1[0]))
for h in range(1,int(in1[1])+1):
    a=list(combinations(sorted(in1[0]),h))
    for i in a:
            print(''.join(list(i)).upper())
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT 
from itertools import combinations
in1=input().split(' ')
a=list(combinations(sorted(in1[0]),int(in1[1])))
for i in a:
    print(''.join(list(i)).upper())
