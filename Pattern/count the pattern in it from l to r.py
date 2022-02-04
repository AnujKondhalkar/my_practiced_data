'''def count_substring(string, sub_string):
    l=[]
    m=[]
    n=[]
    s=string
    for i in s:
        l.append(i)
        #print(l)
    x=len(l)    
    for j in range(x):
        m.append(l[j:x])
        n.append(''.join(m[[j][0]]))     
    return n
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)'''
A = input().strip()
x = input().strip()
count = 0
for i in range(len(A) - len(x) + 1):
    if A[i:i+len(x)] == x:
        count += 1
print count

def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string)-len(sub_string)+1):
        l = i
        for j in range(0, len(sub_string)):
            if string[l] == sub_string[j]:
                l +=1
                if j == len(sub_string)-1:
                    count = count + 1
                else:
                    continue
            else:
                break
            
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
