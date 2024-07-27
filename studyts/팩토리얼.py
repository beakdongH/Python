def f(a):
    if(a==1):
        return
    global m
    m=m*a
    f(a-1)
n,k = map(int,input().split())
m=1
f(n)
iii = m
m=1
f(k)
kkk = m

print(iii,kkk)