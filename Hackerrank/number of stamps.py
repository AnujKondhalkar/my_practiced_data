# Enter your code here. Read input from STDIN. Print output to STDOUT
num=int(input())
my_set=set()
for i in range(num):
    stamp_country=str(input())
    my_set.add(stamp_country)
print(len(my_set))
