# Enter your code here. Read input from STDIN. Print output to STDOUT
stdin1=int(input())
a=set(input().split()[0:stdin1])  
stdin2=int(input())
b=set(input().split()[0:stdin2])
print('\n'.join(sorted(a^b,key=int)))
