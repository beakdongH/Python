nlist = list(map(int, input().split()))

sum=0
for i in range(len(nlist)):
    if(nlist[i]%2!=0): sum+=nlist[i]
if(sum==0): print('-1')
else: print(sum)
