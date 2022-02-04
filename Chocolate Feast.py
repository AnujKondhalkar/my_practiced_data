def chocolateFeast(n, c, m):
    # Write your code here
    money = n # 15
    cost_per_bar = c # 3
    wrappers_to_use = m # 2
    '''------------------------------------------'''
    chocolate = money // cost_per_bar
    eaten=0
    wrappers = chocolate
    #print(l)
    while chocolate > 0 :
        eaten += chocolate
        r_w = wrappers % wrappers_to_use
        chocolate = wrappers // wrappers_to_use
        wrappers = r_w+chocolate
    return eaten













if __name__== '__main__':
        
    n=10
    c=2
    m=5
    print(chocolateFeast(n, c, m))

    n=12
    c=4
    m=4
    print(chocolateFeast(n, c, m))


    n=6
    c=2
    m=2
    print(chocolateFeast(n, c, m))

    
    n=15
    c=3
    m=2
    print(chocolateFeast(n, c, m))
