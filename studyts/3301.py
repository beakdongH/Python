def change(n):
    cnt = 0
    arr = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    for i in arr:
        if n//i != 0:
            cnt+=n//i
            n=n%i
    return cnt
a = int(input())
print(change(a))