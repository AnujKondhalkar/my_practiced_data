'''
#!/bin/python3

import math
import os
import random
import re
import sys
if __name__ == '__main__':
# Enter your code here. Read input from STDIN. Print output to STDOUT
    a= input()
    i=0
    j=0
    count=0
    lst=[]
    while i<=len(a)-1:
        if a[i]==a[j]:
            count=count+1
            j=j+1
        else:
            lst.append([a[i],count])
            count=0
            i=j
        if j==len(a):
            lst.append([a[i],count])
            break
    print(lst)
    vect=sorted(lst, key = lambda x: x[1],reverse=True) #2nd element in a lst
    print(vect)
    for i in vect:
        if i[1]==1:
            pass
        else:        
            print(i[0],i[1])
'''
s= input()
Dict={}
for x in sorted(s):
    Dict[x]=Dict.get(x,0)+1   
#Sorting Dict by value & storing sorted keys in Dict_keys.
Dict_keys=sorted(Dict, key=Dict.get, reverse=True)  

for key in Dict_keys[:3]:
    print(key,Dict[key])
