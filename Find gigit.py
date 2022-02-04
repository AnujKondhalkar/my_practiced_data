def findDigits(n):
    # Write your code here
    count=0
    value=n
    while n != 0 :
        remainder = n % 10;
        n //= 10;
        #print(remainder)
        if remainder!=0 and value%remainder==0:
            count+=1
    return count

a=[111,12,1112,124,10]
for n in a:
    print(findDigits(n))


