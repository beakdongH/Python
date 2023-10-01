num = int(input())
a = []

for _ in range(num):
    a.append(int(input()))

def sum(n):
    if n >= 3:
        return(max(sum(n-2) + a[n], sum(n-3) + a[n-1] + a[n]))
    else:
        return(a[n])

print(sum(num-1))