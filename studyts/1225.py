import sys

def input():
    return sys.stdin.readline().rstrip()

a, b = input().split()
a = list(map(int, a))
b = list(map(int, b))

print(sum(a) * sum(b))
