#함수정의
def noname ():
    return 1

a=5
def func():
    global a
    a=3
    return a
print(a)
print(func())
