t = int(input())

for i in range(t):
    cnt=0
    floor = 0
    number = 0
    h,w,n = map(int, input().split())
    
    for k in range(1,w+1):
        for j in range(1,h+1):
            cnt+=1
            if(cnt==n):
                floor = str(j)
                number = str(k)
    if(int(number)<10):
        print(floor+"0"+number)
    else:
        print(floor+number)
    
            
