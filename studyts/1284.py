while True:
    n=input()
    width=0
    if n=='0':
        break
    for i in range(len(n)):
        if '1' in n[i]:
            width+=2
        elif '0' in n[i]:
            width+=4
        else:
            width+=3
    print(width+len(n)+1)
