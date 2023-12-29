def list_sum(n):    #list_num 함수 생성
    value = n
    sum = 0         #변수 value는 n, sum = 0정의
    while True: #무한반복
        if(value == 0): #만약 value 즉, n이 0이면
            break       #무한반복 탈출
        sum = sum+(value%10)    #sum+=value%10 자릿수에 10씩 나누면 1,2,3...번째 숫자가 나온다
        value = value//10   #밸류도같아
    return sum

if __name__ == "__main__":  #메인함수
    i = int(input())    #i값 입력받기
    while True: #무한반복
        if(i<10):   #만약 i가 10보다 작음
            break   #컷 : 10보다 작으면 굳이 쓸 이유가 없음(두자릿수 안넘음)
        i = list_sum(i) #시이작
    print(i)#i출력 우수수수


