def mon(n,cnt):
    global aa cnt
    if n >= 50000:
        cnt += 1
        mon(n % 50000,cnt)
    elif n >= 10000:
        cnt += 1
        mon(n % 10000,cnt)
    elif n >= 5000:
        cnt += 1
        mon(n % 5000,cnt)
    elif n >= 1000:
        cnt += 1
        mon(n % 1000,cnt)
    elif n >= 500:
        cnt += 1
        mon(n % 500,cnt)
    elif n >= 100:
        cnt += 1
        mon(n % 100,cnt)
    elif n >= 50:
        cnt += 1
        mon(n % 50,cnt)
    elif n >= 10:
        cnt += 1
        mon(n % 10,cnt)
    return cnt

n = aa(input())
print(mon(n,0))
