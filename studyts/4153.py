while True:
    x,y,z = map(int,input().split())
    a,b,c = sorted([x,y,z])
    if(x==0 and y==0 and z==0):
        break
    else:
        if((a*a)+(b*b)==(c*c)):
            print("right")
        else:
            print("wrong")