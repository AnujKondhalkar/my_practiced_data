def happyLadybugs(b):
    # Write your code here
    d={}
    for i in b:
        if i not in d:
            d[i]=b.count(i)
    if '_' in d:
        d.pop('_')
        return 'YES' if (all( (i[1]>=2 or d=={}) for i in d.items()))==True else 'NO'
    elif '_' not in d:
        for k,g in groupby(b):
            if len(list(g))==1:
                return 'NO'
                break
        else:
            return 'YES'     
        
               
from itertools import groupby
if __name__ == '__main__':
    k=['RBY_YBR',
       'X_Y__X',
       '__',
       'B_RRBR',
       'AABBC',
       'AABBC_C',
       '_',
       'DD__FQ_QQF',
       'AABCBC']
    
    for b in k:
        print(happyLadybugs(b))
        #(happyLadybugs(b))

