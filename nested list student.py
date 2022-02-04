if __name__ == '__main__':
    lis=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lis.append([name,score])
    num=[]
    names=[]
    for a in lis:
        num.append(a[1])
    print(num,'as a list')    
    num=set(num)
    print(num,'as a set')    
    num=list(num)
    print(num,'as a list from set')    
    num.sort()    
    for a in lis:
        if num[1]==a[1]:
            names.append(a[0])
    names.sort()
    for i in names:
        print(i)
