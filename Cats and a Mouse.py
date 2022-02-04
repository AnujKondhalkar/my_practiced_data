def catAndMouse(x, y, z):
    cat_a=x
    cat_b=y
    mouce=z
    cat_a_mouce=abs(cat_a-mouce)
    cat_b_mouce=abs(cat_b-mouce)
    if cat_a_mouce<cat_b_mouce:        
        s='Cat A'
    elif cat_a_mouce>cat_b_mouce:        
        s='Cat B'
    else:
        s='Mouse C'
    return s

x=5
y=5
z=4
print(catAndMouse(x, y, z))
