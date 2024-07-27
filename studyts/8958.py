n = int(input())

for i in range(n):
    quiz = input()
    cnt=0
    result=0
    for i in quiz:
        if(i=='O'):
            cnt+=1
        else: cnt=0
        result+=cnt
    print(result)
            
