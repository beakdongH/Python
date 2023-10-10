b = []
for i in range(20):
    b.append([])
    for j in range(20):
        b[i].append(0)

n = int(input())

for i in range(n):
    x,y=input().split()
    b[int(x)][int(y)]=1

for i in range(1,20):
    for j in range(1,20):
        print(b[i][j],end=" ")
    print()
