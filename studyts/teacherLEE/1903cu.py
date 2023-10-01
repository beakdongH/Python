def f(a,b):
    if(a>b):
        return
    if(a%2!=0):
        print(a)
    f(a+1,b)
a,b=map(int,input().split())
f(a,b)
