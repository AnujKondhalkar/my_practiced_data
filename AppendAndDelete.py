def appendAndDelete(s, t, k):
    # Write your code here
    l_small=len(s)if len(s)<=len(t) else len(t)
    v=''
    l_total=len(s)+len(t)
    for i in range(1,l_small+1):
        if s[0:i:]==t[0:i:]:
            #print(s[0:i:])
            v=s[0:i:]
            
    if abs(len(s)-len(v))+abs(len(t)-len(v))>k and l_total%2==k%2 or l_total<k:
        return 'Yes'
         
    else:
        return 'No'




s='qwerasdf'
t='qwerbsdf'
k=6
print(appendAndDelete(s, t, k))


s='ashley'
t='ash'
k=2
print(appendAndDelete(s, t, k))


s='abcd'
t='abcdert'
k=10
print(appendAndDelete(s, t, k))


s='y'
t='yu'
k=2
print(appendAndDelete(s, t, k))
