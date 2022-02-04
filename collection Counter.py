from collections import Counter
X=int(input())      #The number of shoes.
Y=list(map(int,input().split(' '))) #The space separated list of all the shoe sizes in the shop.
N=int(input())#the number of customers
my_shoe=(Counter(Y))
#{2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 8: 1, 7: 1, 18: 1}
s_um=0
for _ in range(N): # the space separated values of the 'shoe size' desired by the customer and 'Xi', the price of the shoe.
    size, price=(list(map(int,input().split(' '))))
    #print( size, price)
    if my_shoe[size]:
        s_um+=price
        my_shoe[size]-=1
print(s_um)
       





'''
from collections import Counter
>>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
>>> print (Counter(myList))
Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
>>> print (Counter(myList).items())
dict_items([(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)])


10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
'''
