# s = 'abcde'
# for i in range(len(s) - 1, -1, -1):
#     print(s[i], end='')
# s_re = ''
# for j in s:
#     s_re = j + s_re
# print(s_re)
# list(s)
# s.reverse()
# print(s)

s = input()
for i in range(len(s) - 1, -1, -1):
    print(s[i], end='')