a='<head>l'
l=[]
for i in range(len(a)+1):
    if a[0]=='<':
        if a[i]!='>':
            l.append(a[i+1])
b="".join(l)
print(b)


'''
9
<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">
  <!-- <param name="movie" value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>
'''   
   
