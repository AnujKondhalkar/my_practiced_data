#!/bin/python3

import math
import os
import random
import re
import sys
import pdb
#('A', ['a', 'a', 'b', 'a', 'b'])
#('B', ['a', 'b'])

pdb.set_trace()
def jumpingOnClouds():
    # Write your code here
    d=defaultdict(list)
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    for i in range(n):
        d['A'].append(str(input()))
    M=[]
    O=[]
    v=0
    for i in range(m):
        k=str(input())
        for j in d['A']:
            if k==j:
                #print(j,' ',v+1)
                M.append(str(v+1))
                v+=1
            else:
                v+=1
        if k not in d['A']:
            M.append(str(-1))                
        v=0
        O.append(M)
        M=[]            
    return O    
from collections import defaultdict
if __name__ == '__main__':
    result=jumpingOnClouds()
    #print(result)
    for i in result:
        print(' '.join(i))
