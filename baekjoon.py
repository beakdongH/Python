#2557
print("Hello World!")

#1000
a, b = map(int, input().split())
print(a+b)

#1001
a, b = map(int, input().split())
print(a-b)

#10998
a, b = map(int, input().split())
print(a*b)

#1008
a, b = map(int, input().split())
print(a/b)

#10869
a, b = map(int,input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)

#1330
a, b = map(int,input().split())
if a>b:
    print(">")
if a>b:
    print("<")    
if a==b:
    print("==")    

#9498
a = int(input())
if (100>=a>=90):
    print("A")
elif (90>a>=80):
    print("B")
elif (80>a>=70):
    print("C")
elif (70>a>=60):
    print("D")
else:
    print("F")
  
#2753
a = int(input())
if(a%4==0 and a%100!=0) or a%400==0:
    print("1")
else:
    print("0")
