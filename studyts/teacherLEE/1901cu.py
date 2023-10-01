def f(a):
    if(a==0):
        return
    else:
        f(a-1)
        print(a)
n = int(input())
f(n)

