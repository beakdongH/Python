x,y,w,h = map(int,input().split())

if(w-x>=h-y):
    if(y-0<h-y):
        print(y-0)
    else:
        print(h-y)

else:
    if(x-0<w-x):
        print(x-0)
    else:
        print(w-x)
