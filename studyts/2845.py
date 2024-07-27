l,p = map(int,input().split())
guys = list(map(int,input().split()))

fill = l*p

for i in range(5):
    print(guys[i]-fill,end=' ')
