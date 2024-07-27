etc=[]
cnt=0
for i in range(10):
    a = int(input())
    
    if a%42 not in etc:
        etc.append(a%42)
        cnt+=1
print(cnt)
    
