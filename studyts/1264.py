vowels = ['a', 'e', 'i', 'o', 'u']

while True:
    text = input()
    if text == '#':
        break
    
    cnt=0
    for i in text:
        if i.lower() in vowels:
            cnt+=1
    
    print(cnt)
