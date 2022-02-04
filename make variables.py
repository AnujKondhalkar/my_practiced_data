N,M= [int(x) for x in input().split()][:2]
#The next 'N' lines contains 'M' space separated integers
string='var'
lst0=[]
lst1=[]
for i in range (N):
    lst0.append(string+str(i))
for j in range (len(lst0)):
    lst0[j] = [int(x) for x in input().split()]
    lst1.append(lst0[j])
print(lst1)
