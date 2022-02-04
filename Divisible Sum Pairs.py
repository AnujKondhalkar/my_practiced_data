from itertools import combinations
def divisibleSumPairs(n, k, ar):
    count=0
    # Write your code here
    l_comb=list(combinations(ar,2))
    for ele in l_comb:
        if (ele[0]+ele[1])%k==0:
            #print(ele)
            count+=1
    return count  
ar=[1,2,3,4,5,6]
n=len(ar)
k=3
result=divisibleSumPairs(n, k, ar)
print(result)





'''
100 41
20 40 78 58 88 84 49 10 75 49 99 30 7 15 80 29 43 94 99 58 23 57 84 65 63
86 37 10 44 79 45 79 17 40 7 27 74 70 92 76 52 73 18 49 29 19 7 43 11 41
7 26 49 61 75 37 33 28 6 5 70 47 58 74 66 26 22 90 25 15 91 96
8 17 83 10 67 13 62 63 98 5 94 1 32 46 22 5 16 62 56 57 51 19 15 65 44
72 59 20

'''
