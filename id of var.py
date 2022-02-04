y=5
print(id(y),'   ',y)

def d():
    global y
    y=6
    print(id(y),'   ',y)
    print(id(y),'   ',globals()['y'])

d()

print(id(y),'   ',y)
