n = input()
nre = int(str(n)[::-1])
cnt = 0
for i in range(len(n)):
    cnt += int(n[i])

print(nre)
print(cnt)
