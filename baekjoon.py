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

#2480
a,b,c = map(int, input().split())

if(a==b==c): print(10000+a*1000)

elif(a==b or a==c): print(1000+a*100)
elif(b==c): print(1000+b*100)

else:
    if(a>b):
        tmp = a
        a = b
        b = tmp
    if(b>c):
        tmp = b
        b = c
        c = tmp
    if(a>b):
        tmp = a
        a = b
        b = tmp 
    print(c*100)

#2739
n = int(input(""))
i = 1
while i<10:
  print(n,"*",i,"=",i*n)
  i+=1

#25314
a = int(input())
b=a//4
print("long "*b + "int")

#2438
a = int(input())
for i in range(1,a+1):
    print("*"*i)

#2439
a = int(input())
for i in range(1,a+1):
    a=a-1
    print(" "*(a)+"*"*i)

#10952
while True:
    a,b = map(int, input().split())
    if a==0 and b==0:
        break
    else:
        print(a+b)

#10951
while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except EOFError:
        break

#27866
a = input()
b = int(input())
print(a[b-1])

#2743
a = input()
print(len(a))

#11720
n = int(input())
b = input()
a = list(map(int, b))
print(sum(a))

#11718
while(True):
    try:
        a = input()
        if(a==""):
            break
        print(a)
    except:
        break
        
#2675
n = int(input())
for i in range(n):
    a,b = input().split()
    for j in (b):
        print(j*int(a),end="")
    print()

#11382
a,b,c = map(int, input().split())
print(a+b+c)

#8393
n =int(input())
a=0
for i in range(1,n+1):
    a+=i
print(a)

#18108
n = int(input())
n -= 543
print(n)

#11021
n = int(input())
for i in range(n):
    a,b = map(int, input().split())
    print("Case #{}: {}".format(i+1, a+b))

#1152
sen=input().split()         #공백 짤루
print(len(sen))             #그리고 sen의 길이재서 개수 알수있

#1546
n = int(input())
list = list(map(int, input().split()))

a = max(list)
avg = 0

for i in range(n):
    avg += (list[i]/a)*100

print(avg/n)

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

#2562
nlist = []
for i in range(9):
    a =  int(input())
    nlist.append(a)
print(max(nlist))
print(nlist.index(max(nlist))+1)

#10950
t = int(input())
for i in range(1,t+1):
    a,b = map(int, input().split())
    print(a+b)

#2440
a = int(input())
for i in range(1,a+1):
    print("*"*a)
    a=a-1

