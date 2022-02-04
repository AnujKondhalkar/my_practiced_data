# Enter your code here. Read input from STDIN. Print output to STDOUT
in1 = int(input())
in2 = int(input())
a=divmod(in1,in2)
for i in range(len(a)):
    print(a[i])
print(a)
