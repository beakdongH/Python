#숫자로테이션
def rot(arr):
    leng = len(arr)
    for i in range(1,leng):
        for j in range(i,leng+i):
            print(arr[j%leng],end=" ")
        print()

a=int(input())
arr = list(map(int,input().split()))
print(*arr)
rot(arr)

#지피티야 고마워
def rot(arr):
    leng = len(arr)
    for i in range(1, leng):
        temp = arr.pop()
        arr.append(temp)
        print(*arr)

a = int(input())
arr = list(map(int, input().split()))
print(*arr)
rot(arr)
