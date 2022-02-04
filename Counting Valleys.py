import itertools
def countingValleys(steps, path):
    # Write your code here
    for (key,group) in itertools.groupby(path):
        print (key,len(list(group)))
            
def countingValleys(steps, path):
    # Write your code here
    valley=0
    level=0
    for i in path:
        if i=='U':
            level+=1
        if i=='D':
            level-=1
        if level==0 and i=='U':
            valley+=1
    print(valley)
            




    
steps=8
path='UDDDUDUU'
countingValleys(steps, path)
