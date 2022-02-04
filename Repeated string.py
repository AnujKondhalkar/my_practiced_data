def repeatedString(s, n):
    # Write your code here
    
    j=(n//len(s))*s.count('a')
    k=s[:n % len(s)]

    print(j)
    print(k)


'''
s='abcac'
n=10
print(repeatedString(s, n))

s='a'
n=1000000000000
print(repeatedString(s, n))
'''
s='aba'
n=15
print(repeatedString(s, n))
