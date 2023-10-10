def plusn(a):
    if len(a)==0:
        return 0
    num = a.pop()
    return num+plusn(a)

naye = list(map(int, input().split()))
result = plusn(naye)
print(result)