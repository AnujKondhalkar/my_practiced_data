if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(integer_list)
    a=list(integer_list)
    t = tuple(integer_list)
    print(a,t)
    print(t)
    print(hash(t))
