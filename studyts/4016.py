def gcd(a,b,c):
    if b == 0 and c == 0:
        return a
    if b == 0:
        return gcd(a, c, 0)
    return gcd(b, a % b, c % a)

a,b,c = map(int, input().split())
print(gcd(a,b,c))

