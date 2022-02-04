def average(array):
    a=0
    i=0
    r=0
    j=set(array)
    # your code goes here
    if i<=len(j):
        a=a+j[i]
        i=i+1
    else:
        a= a/len(j)
    return a
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
