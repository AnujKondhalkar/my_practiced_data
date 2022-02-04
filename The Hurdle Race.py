def hurdleRace(k, height):
    # Write your code here
    j=max(height)-k
    return j if j>=1 else 0 
    



k=1
height=[1,2,3,3,2]
print(hurdleRace(k, height))
print('ok')

k=7
height=[2,5,4,5,2]
print(hurdleRace(k, height))

