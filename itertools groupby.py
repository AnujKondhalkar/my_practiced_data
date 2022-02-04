from itertools import groupby
p='AABCBC'
for k,g in groupby(p):
    #print((len(list(g)),k))
    #print(len(list(g)),k)
    print(len(list(g)),k)
