a,b = map(int, input().split())

def so(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def dea(a, b):
    return a*b//so(a, b)

print(so(a,b))
print(dea(a,b))