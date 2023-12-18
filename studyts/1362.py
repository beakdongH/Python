n = int(input())

num = n*(n+1)//2

for i in range(n,0,-1):
    for j in range(n,i-1,-1):
        print(num,end=" ")
        num=num-1
    print()