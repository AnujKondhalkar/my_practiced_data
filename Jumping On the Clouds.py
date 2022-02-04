def jumpingOnClouds(c):
    # Write your code here
    count=0;
    i=0;
    while(i<len(c)-1):
        if(i+2<len(c) and c[i+2]!=1):
            count+=1
            i=i+2       
        else:
            count+=1
            i+=1             
    return count


c=[0,1,0,0,0,1,0]            
print(jumpingOnClouds(c))# 4 , 3....ans 3


c=[0,0,0,0,1,0]            
print(jumpingOnClouds(c))# 4 , 3....ans 3

c=[0,0,1,0,1,0]            
print(jumpingOnClouds(c))# 4 , 3....ans 3


c=[0,0,0,0,1,0]            
print(jumpingOnClouds(c))#3....ans 3

