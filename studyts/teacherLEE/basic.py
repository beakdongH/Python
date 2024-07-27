#1~100 짝수합
a = int(input())
result = 0
for i in range(2,a+1,2):
    result+=i
print(result)