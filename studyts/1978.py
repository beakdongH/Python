n = int(input())
lst = list(map(int,input().split()))
sum=0


for i in lst:
    cnt = 0
    if i>1:
        for j in range(2,i):
            if(i%j==0): cnt+=1
        if(cnt == 0): sum+=1
    
print(sum)