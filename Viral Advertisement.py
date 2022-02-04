def viralAdvertising(n):
    # Write your code here
    people=5; shared=people; liked=0; cumulative=0; 
    for day in range(1,n+1):
        liked=(shared//2)
        cumulative+=liked
        shared=liked*3   
    return(cumulative)


n=5 
print(viralAdvertising(5))

