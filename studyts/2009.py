k,n = map(int, input().split())
s=0
while k>=n:
    s+=1
    k-=n
    k+=1
print(s)