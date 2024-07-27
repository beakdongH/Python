def f(a):
    result = 1
    for i in range(2,a+1):
        result *= i
    return result


n,k = map(int,input().split())

fac_n = f(n)
fac_k = f(k)
fac_nk = f(n-k)

sum = fac_n/(fac_nk*fac_k)

print(int(sum))
