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

#14681
x = int(input())
y = int(input())

if (x>0 and y>0): print("1")
elif (x<0 and y>0): print("2")
elif (x<0 and y<0): print("3")
else: print("4")

#2884
h,m = map(int, input().split())

if m - 45<0 :
    m = 60-(45-m)

    
    h = h-1
    if h<0 :
        h = 23

elif m-45>=0 :
    m = m-45
print(h, m)
