# Enter your code here. Read input from STDIN. Print output to STDOUT
a= input()
i=0
j=0
count=0
s=''
while i<=len(a)-1:
    if a[i]==a[j]:
        count=count+1
        j=j+1
    else:
        s=s+'('+str(count)+', '+a[i]+')'+' '
        count=0
        i=j
    if j==len(a):
        s=s+'('+str(count)+', '+a[i]+')'+' '
        print(s)
        break
