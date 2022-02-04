# Enter your code here. Read input from STDIN. Print output to STDOUT
def like_unlike(a,j,k):
    count=0
    for i in range(len(a)):
        if a[i] in j:
            count=count+1        
    for i in range(len(a)):
        if a[i] in k:
            count=count-1    
    return count
if __name__ == '__main__':
    y,z=[int (x) for x in input().split(' ')][0:2]
    a=[int (x) for x in input().split(' ')]
    j={int (x) for x in input().split(' ')}
    k={int (x) for x in input().split(' ')}
    print(like_unlike(a,j,k))
