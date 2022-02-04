def minion_game(string):
    # your code goes here
    Stuart_sc=0
    Kevin_sc=0
    for i in range(len(string)):
        if string[i] not in 'AEIOU':
            Stuart_sc=Stuart_sc+len(string)-i      
        else:
            Kevin_sc=Kevin_sc+len(string)-i
    if Kevin_sc>Stuart_sc:
        print('Kevin',Kevin_sc)
    elif Kevin_sc<Stuart_sc:
        print('Stuart',Stuart_sc)
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)

#1
'''
string=input()
st=''
Stuart_sc=0
Kevin_sc=0
for i in range(len(string)):
    s_st=string[i::]
    if s_st[0] not in 'AEIOU':
        Stuart_sc=Stuart_sc+len(string)-i      
    else:
        Kevin_sc=Kevin_sc+len(string)-i
if Kevin_sc>Stuart_sc:
    print('Kevin',Kevin_sc)
elif Kevin_sc<Stuart_sc:
    print('Stuart',Stuart_sc)
else:
    print('Draw')
'''


#2
'''
string=input()
st=''
Stuart_sc=0
Kevin_sc=0
for i in range(len(string)):
    s_st=string[i::]
    if s_st[0] not in 'AEIOU':
        Stuart_sc=Stuart_sc+len(s_st)        
    else:
        Kevin_sc=Kevin_sc+len(s_st)
if Kevin_sc>Stuart_sc:
    print('Kevin',Kevin_sc)
elif Kevin_sc<Stuart_sc:
    print('Stuart',Stuart_sc)
else:
    print('Draw')
'''
   
#3


'''
string=input()
st=''
Stuart_sc=0
Kevin_sc=0
for i in range (len(string)):
    sst=string[i::]
    for j in range(len(sst),0,-1):
            l=sst[0:j:]
            if l[0] in 'AEIOU':
                Kevin_sc=Kevin_sc+1
            else:
                Stuart_sc=Stuart_sc+1
                
if Kevin_sc>Stuart_sc:
    print('Kevin',Kevin_sc)
elif Kevin_sc<Stuart_sc:
    print('Stuart',Stuart_sc)
else:
    print('Draw')
'''
