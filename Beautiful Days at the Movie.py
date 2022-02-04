def beautifulDays(i, j, k):
    # Write your code here
    count=0
    for i in range(i,j+1):
        if abs(i-int(str(i)[::-1]))%k==0:
            count+=1
    return count


i=20
j=23
k=6
print(beautifulDays(i, j, k))
num = 123456
print(str(num)[::-1])
