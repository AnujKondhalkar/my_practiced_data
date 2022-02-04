if __name__ == '__main__':
    n = int(input())
    arr = (map(int, input().split()))
    a=list(arr)
    a.sort()
    print(a[a.index(max(a))-1])
