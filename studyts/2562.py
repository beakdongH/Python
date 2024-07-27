nlist = []
for i in range(9):
    a =  int(input())
    nlist.append(a)
print(max(nlist))
print(nlist.index(max(nlist))+1)
