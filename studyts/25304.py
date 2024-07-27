total = int(input())
cnt = int(input())
result=0

for i in range(cnt):
    a,b = map(int,input().split())
    result+=(a*b)

if (result == total): print("Yes")
else: print("No")
