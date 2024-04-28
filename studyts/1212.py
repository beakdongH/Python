a = input()
b = bin(int(a,8))[2:]
print(b if b != '0' else '0')
