from math import sqrt,floor,ceil
def squares(a, b):
    # Write your code here
    return floor(sqrt(b)) - ceil(sqrt(a)) + 1
        

a=24
b=49
print(squares(a, b))
