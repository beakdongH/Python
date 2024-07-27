n = int(input())
original = n
cnt =0
while 1:
    ten_num = n//10
    one_num = n%10
    a = (ten_num+one_num)%10
    n = one_num *10 + a
    cnt+=1

    if n == original:
        break
print(cnt)
