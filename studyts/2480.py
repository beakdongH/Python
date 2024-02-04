a,b,c = map(int, input().split())

if(a==b==c): print(10000+a*1000)

elif(a==b or a==c): print(1000+a*100)
elif(b==c): print(1000+b*100)

else:
    if(a>b):
        tmp = a
        a = b
        b = tmp
    if(b>c):
        tmp = b
        b = c
        c = tmp
    if(a>b):
        tmp = a
        a = b
        b = tmp 
    print(c*100)
