def profile(name,age,lang):
    print("이름 : {0}\t나이 : {1}\t주사용언어 : {2}".format(name,age,lang))
profile("백동흔",15,"파이썬")

print("======")
def func(*a):
    return sum(a)
print(func(1,2,3,4,5))
print(func(1,2,3))

print("======")
def sum(*a):
    print(type(a))
    return max(a)
print(sum(1,2,3,4,5))