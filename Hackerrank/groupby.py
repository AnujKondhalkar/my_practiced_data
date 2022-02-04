groups = ['aaaabbbbcccddd']
uniquekeys = ['aaa']
data = sorted(data, key=keyfunc)
for k, g in groupby(data, keyfunc):
    groups.append(list(g))      # Store group iterator as a list
    uniquekeys.append(k)
print(groups)
print(uniquekeys)

