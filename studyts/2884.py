h,m = map(int, input().split())
if m - 45<0 :
    m = 60-(45-m)
    h = h-1
    if h<0 :
        h = 23
elif m-45>=0 :
    m = m-45
print(h, m)
