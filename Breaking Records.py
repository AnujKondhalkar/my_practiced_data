def breakingRecords(scores):
    # Write your code here
    hi=scores[0]
    lo=scores[0]
    Min_score=0;
    Max_score=0;
    
    for i in range(1,len(scores)):
        
        if scores[i]>hi:
            
            Max_score+=1
            hi=scores[i]
            
        elif scores[i]<lo:
            
            Min_score+=1
            lo=scores[i]

    return [Max_score,Min_score]


scores=[12,24,10,24]
print(breakingRecords(scores))

scores=[10,5,20,20,4,5,2,25,1]
print(breakingRecords(scores))

scores=[3,4,21,36,10,28,35,5,24,42]
print(breakingRecords(scores))
