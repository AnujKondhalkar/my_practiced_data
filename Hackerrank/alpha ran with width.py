'''
al=5
l=[]
for i in range (0,al+1):
    j=chr(97+al-i)
    if i<=al-2:
        p='-'
    else:
        p=''
    l.append(j+p)
m=''.join(l)
for i in range (5):
    print(m.center(i*4-3,'-'))





#--a-b-c-d-e--
'''

al=4
l=[]
for i in range(al):
    for j in range (i,al):
        print(chr(97+al-j))
