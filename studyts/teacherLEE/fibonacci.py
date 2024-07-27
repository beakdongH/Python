#피보나치 수열
def fibo(n):                        # 함수 정의
    if n==0 or n ==1:               # 0 과 1일 때는 따로 계산이 필요 없으니
        return n                    # 0 일 때는 0, 1일 때는 1 을 return한다
    else:                           # 위의 조건이 아닐 때는
        return fibo(n-1)+fibo(n-2)  # 입력된 n값에서 피보나치 수열 계산을 통해 주루루룩
    
a = int(input())                    
print(fibo(a))                      # fibo 의 n을 입력받은 n으로 해, 위 함수를 이용한다.
