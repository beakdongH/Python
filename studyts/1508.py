arr = [[0]*20]*20
n = int(input())

for i in range(n+1):
    for j in i:
        print(j,end=" ")
    print()