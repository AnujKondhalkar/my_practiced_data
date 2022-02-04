a= 'abbcccddd'
#   123456789
print(a,'==>',len(a))
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

'''##hackerrank       
#a=input()
s=''
for i in range(0,len(a)):
    if i!=0:
        if a[i]==a[i-1]:  
            continue
    p=0
    for j in range(i,len(a)):
        if a[i]==a[j]:
            p+=1
        else:
            break
    s+='('+str(p)+', '+a[i]+')'+' '
print(s)
'''     
    
    
