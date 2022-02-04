import numpy
N,M= [int(x) for x in input().split()][:2]
#The next 'N' lines contains 'M' space separated integers
lst1=[]
for j in range (N):
    lst1.append([int(x) for x in input().split()])
my_array=numpy.array(lst1)
result=numpy.sum(my_array, axis = 0)
print(numpy.prod(result, axis = 0))
