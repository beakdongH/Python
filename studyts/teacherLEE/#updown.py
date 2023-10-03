#updown
import random as r
a = r.randint(1,100)
count=0
print(a)
while True:
    try:
        n = int(input())
        if (n==a):
            print(a)
            print(count)
        elif (n<a):
            print("UP")
            count+=1
        elif (n>a):
            print("DOWN")
            count+=1
    
    except:
        print("디씨 ")