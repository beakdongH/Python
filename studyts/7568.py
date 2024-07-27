n = int(input())
lst=[]
rank=[]

for i in range(n):
    w,h = map(int,input().split())
    lst.append([w,h])

for i in range(n):
    cnt=0
    for j in range(n):
        if(lst[i][0]<lst[j][0] and lst[i][1] < lst[j][1]):
            cnt+=1
    rank.append(cnt+1)

for i in rank:
    print(i)