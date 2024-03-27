h,m,s = map(int,input().split())
plus = int(input())

s+=plus%60
plus = plus//60
if s>=60:
    s-=60
    m+=1

m+=plus%60
plus=plus//60
if m>=60:
    m-=60
    h+=1

h+=plus%24
if h>=24:
    h-=24

print(h,m,s)