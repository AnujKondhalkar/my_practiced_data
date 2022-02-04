#!/bin/python3
import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
    
st=''
for i in range(m):
    for j in range(n):
        st=st+matrix[j][i]
#print(st)

#OR
print(re.sub(r'\b[^a-zA-Z0-9]+\b',r' ', st))
print(re.sub(r"(?<=\w)+([^\w])+(?=\w)", " ", st))

'''
for z in zip(*matrix):
    b += "".join(z)
'''

'''
7 3
lst=[
     'Tsi',
     'h%x',
     'i #',
     'sM ',
     '$a ',
     '#t%',
     'ir!'
     ]
'''
#'lst[COLOMON][ROW]'
#j=row
#i =colomon
'''
7 3
Tsi
h%x
i #
sM 
$a 
#t%
ir!
'''
