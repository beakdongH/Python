# a,b,c = map(int, input().split())
# while b!=0:
#     a, b = b, a % b
#     #r = a % b
# while c!=0:
#     a, c = c, a % c
# print(a)

def gcd(a,b,c):
    if b == 0 and c == 0:
        return a
    if b == 0:
        return gcd(a, c, 0)
    return gcd(b, a % b, c % a)

a,b,c = map(int, input().split())
print(gcd(a,b,c))