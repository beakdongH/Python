def f(a):
    if(a==1):
        return
    global m
    m=m*a
    f(a-1)
n = int(input())
m=1
f(n)
print(m)