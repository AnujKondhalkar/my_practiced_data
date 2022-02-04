def serviceLane(width, cases):
    # Write your code here
    l=[]
    for i in cases:
        print()
        l.append(min(width[i[0]:i[1]+1:]))        
    return l
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    t = int(first_multiple_input[1])
    width = list(map(int, input().rstrip().split()))
    cases = []
    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))
    result = serviceLane(width, cases)
    print('\n'.join(map(str, result)))
    #print('\n')
'''
INPUT
5 5
1 2 2 2 1
2 3
1 4
2 4
2 4
2 3

my OUTPUT expected OUTPUT

 2              2
 2              1
 2              1
 2              1
 2              2
'''






'''
def serviceLane(n, cases):
    # Write your code here
    #width=[2, 3, 1, 2, 3, 2, 3, 3]
    for i in cases:
        print(min(width[i[0]:i[1]:+1]))



n=8
cases = [[0, 3], [4, 6], [6, 7], [3, 5], [0, 7]]
serviceLane(n, cases)
'''
