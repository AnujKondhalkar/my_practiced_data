w = 5
h = 5

ls = []

for i in range(h):
 row = []
 for j in range(w):
  row.append(i)
 ls.append(row)

print (ls)

ls[2][3] = 'foo'

print (ls)
