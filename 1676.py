def f(a):
    global m
    if a == 1:
        return
    m *= a
    f(a-1)

n = int(input())
if n == 0:
    print(0)

else:
    m = 1
    f(n)
    number = str(m)
    cnt = 0
    for i in range(len(number)-1,-1,-1):
        if number[i]!='0':
            break
        cnt += 1
    print(cnt)
