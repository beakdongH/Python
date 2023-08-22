//6001
print("Hello")

//6002
print("Hello World")

//6003
print("Hello") 
print("World")

//6004
print("'Hello'");

//6005
print('"Hello World"');

//6006
print("\"!@#$%^&*()\'")

//6007
print("\"C:\\Download\\\'hello\'.py\"")

//6008
print("print(\"Hello\\nWorld\")")

//6009
a = input()
print(a)

//6010
n = input()
n = int(n)
print(n)

//6011
f = input()
f = float(f)
print(f)

//6012
a = input() 
b = input()
a=int(a)
b=int(b)
print(a)
print(b)

//6013
a = str(input()) 
b = str(input())
print(b)
print(a)

//6014
f = input()
f = float(f)
print(f)
print(f)
print(f)

//6015
a, b = input().split()
a=int(a)
b=int(b)
print(a)
print(b)

//6016
a,b = input().split()
a=str(a)
b=str(b)
print(b,a)

//6017
s = input()
print(s, s, s)

//6018
a, b = input().split(':')
print(a, b, sep=':')

//6019
a, b,c = input().split('.')
print(c, b,a, sep='-')

//6020
a, b = input().split('-')
print(a+b)

//6021
s = input()
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

//6022
s=input()
print(s[0:2])
print(s[2:4])
print(s[4:6])

//6023
a,b,c = input().split(':')
print(b)

//6024
w1, w2 = input().split()
s = w1 + w2
print(s)

//6025
a, b = input().split()
c = int(a) + int(b)
print(c)

//6026
a = float(input())
b = float(input())
print(a+b)

//6027
a = int(input())
print('%x'%a)

//6028
a = int(input())
print("%X" %a)

//6029
a = input()
n = int(a, 16)
print('%o' % n)  

//6030
n = ord(input())
print(n)

//6098
d=[]
for i in range(20) :
  d.append([])
  for j in range(20) : 
    d[i].append(0)

for i in range(19) :
  a = input().split()
  for j in range(19) :
    d[i+1][j+1] = int(a[j])

n = int(input())
for i in range(n) :
  x,y=input().split()
  x=int(x)
  y=int(y)
  for j in range(1, 20) :
    if d[j][y]==0 :
      d[j][y]=1
    else :
      d[j][y]=0

    if d[x][j]==0 :
      d[x][j]=1
    else :
      d[x][j]=0

for i in range(1, 20) :
  for j in range(1, 20) :
    print(d[i][j], end=' ')
  print()

//6069
sc = {'A': 'best!!!', 'B': 'good!!', 'C': 'run!', 'D': 'slowly~'}
cal = input()
print(sc.get(cal, 'what?'))

//6070
m={1:'spring',2:'summer',3:'fall'}
a=int(input())
a=a//3
print(m.get(a,"winter"))

//6071
a = int(input())
while a!=0:
    a-=1
    print(a)

//6097
h,w=map(int,input().split())

b=[]
for i in range(h+1):
    b.append([ ])
    for j in range(w+1):
        b[i].append(0)
n = int(input())
for i in range(n):
    l,d,x,y = map(int,input().split())
    if int(d)==0:
        for j in range(int(l)):
            b[int(x)][int(y)+j]=1
    else:
        for j in range(l):
            b[int(x)+j][int(y)]=1
    
for i in range(1,h+1):
    for j in range(1,w+1):
        print(b[i][j], end=' ')
    print()
