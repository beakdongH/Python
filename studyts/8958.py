a = int(input())

for i in range(a):
    result = input()
    score=0
    cnt=0
  
    for j in result:
        if j =='O':
            cnt +=1
            score +=cnt
        else:
            cnt = 0
    
    print(score)
