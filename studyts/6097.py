h,w=map(int,input().split())

b=[]
for i in range(h+1):
    b.append([ ])
    for j in range(w+1):
        b[i].append(0)
n = int(input())
for i in range(n):
    l,d,x,y = map(int,input().split())
    if int(d)==0:
        for j in range(int(l)):
            b[int(x)][int(y)+j]=1
    else:
        for j in range(l):
            b[int(x)+j][int(y)]=1
    
for i in range(1,h+1):
    for j in range(1,w+1):
        print(b[i][j], end=' ')
    print()
