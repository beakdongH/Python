a = int(input())
b = list(map(int, input().split()))
result = list(0 for i in range(24))

for i in range(a):
    result[b[i]] += 1

for j in range(1, 23):
    print(result[j],end=" ")
