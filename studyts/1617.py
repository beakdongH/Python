s = input()
s_re = s[::-1]
sum = int(s) + int(s_re)
if str(sum) == str(sum)[-1]:
    print("YES")
else:
    print("NO")
