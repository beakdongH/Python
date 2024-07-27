n = int(input())
text = []

for i in range(n):
    text.append(input())

sett = set(text)	
llist = list(sett)	

llist.sort()
llist.sort(key = len)

for i in llist:
    print(i)