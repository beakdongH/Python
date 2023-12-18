n=int(input())
nre = int(str(n)[::-1])
sum = n+nre
sumre = int(str(sum)[::-1])
if(sum==sumre):
    print("YES")
else:
    print("NO")