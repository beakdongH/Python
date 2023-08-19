ame = int(input("아메리카노 판매 개수"))
cafe = int(input("카페라떼 판매 개수"))
capu = int(input("카푸치노 판매개수"))
chong = ame*2000+capu*4000+cafe*3000

print("총매출은",chong,"원입니다")

===========================조건문=============================

year = int(input("연도를 입력하십시오"))

if (year%4 == 0) and (year%100 != 0) or (year%400 == 0):
  print(year,"년은 윤년입니다")
else :
  print(year,"년은 윤년이 아닙니다")
  
==============================================================

age = int(input("나이를 입력하십시오"))

if age >= 16 :
  print("영화관람이 가능합니다")
  print("영화 가격은 10000원입니다")

else :
  print("이 영화 관람이 불가능합니다")
  print("다른 영화를 보시겠습니까?")

==============================================================

su = int(input("정수를 입력하십시오"))

if su > 0:
  print("양수입니다")
if su < 0:
  print("음수입니다")

==============================================================

su = int(input("정수를 입력하십시오"))

if su%2 == 1 :
  print("홀수입니다")
if su % 2 == 0 :
  print("짝수입니다")

==============================================================

a = int(input("성적을 입력하십시오"))

if a >= 90:
  print("학점: A")
elif a >= 80:
  print("학점:B")
elif a >= 70:
  print("학점:C")
else :
  print("학점:F")
print("수고하셨습니다!")

==============================================================

kg = float(input("몸무게를 kg단위로 입력하세요"))
tall = float(input("키를 미터(m) 단위로 입력하십시오"))
bmi = kg/(tall*tall)

print(bmi)
if bmi > 27.77 :
  print("비만입니다")
elif  bmi > 24.74 :
  print("과체중입니다")
elif  bmi > 16.83 :
  print("정상입니다")
else :
  print("저체중입니다")

==============================================================

import random
print(random.randint(1,20))
print(random.choice([1,2,5,7]))
print(random.randrange(2))
print(random.sample(range(1,50),5))

==============================================================

import random
a = random.choice(["left", "right", "center"])
sube =input("어디를 수비하시겠습니까?[left, right, center]")

if sube == a :
  print("수비에 성공하였습니다")

else :
  print("수비에 실패하였습니다")

==============================================================

import random

a = random.randrange(2)
if a == 0:
  print("뒷면입니다!")
if a == 1:
  print("앞면입니다!")
print("게임이 종료되었습니다")

==============================================================

import random as r
a = r.randint(1,5)
b = r.randint(1,5)

print(a,b)
c = int(input("두수의 합계를 입력하세요"))
if c == a+b :
  print("정답입니다")
else :
  print("오답입니다")

==============================================================

===========================반복문=============================

import random as r
i = 0
while i<5:
  print(r.randint(1,45),end=" ")
  i+=1

==============================================================

import random as r
ran = r.randint(1,100)
count = 0

while True:
  dap=int(input("1~100 사이의 숫자를 추측해 보세요"))
  count+=1
  if dap > ran :
    print("입력한 수보다 작습니다")
  elif dap < ran :
    print("입력한 수보다 큽니다")
  else :
    print("축하합니다! 정답입니다")
    print("시도횟수 :",count,"정답:",ran)
    break

==============================================================

dan = int(input("단수를 입력하십시오"))
i = 1
while i<10:
  print(dan,"x",i,"=",i*dan)
  i+=1

==============================================================

i = 1
a = 0
while i<11:
  a+=i
  i+=1
print(a)

==============================================================

i=1
a=0
while i<100:
  if i%3==0:
    print(i,end=" ")
  i+=1

==============================================================

for i in range(10):
  print(i)

==============================================================

a=1
for i in range(20):
  print(i)

==============================================================

a = int(input("반복횟수를 입력하세요"))
sum=0
for i in range(a):
  x = int(input("정수를 입력하세요"))
  sum+=x
s=sum/a
print("합계",sum,"평균",s)

==============================================================

import random as r
sum=0
for i in range(10):
  x = r.randint(1,100)
  sum+=x
f=sum/10
print("합계",sum,"평균",f)

==============================================================

k =0
for i in [1, 2, 5, 7, 9]:
  k+=i
y=k/5
print("합계",k,"통계",y)

==============================================================

import random
coun=0
k=0
for i in range(5):
  x=random.randint(1,50)
  y=random.randint(1,50)
  print(x,"+",y,"= ?",end=" ")
  n=int(input())
  if n == x+y:
    print("정답입니다!")
    coun+1
  else :
    print("틀렸습니다")
    k+1
print("한번만에 맞힌 개수",coun,"개 입니다")

==============================================================

for i in range(6):
  for x in range(1,i+1):
    print("*",end=" ")
  print(" ")

==============================================================

for i in range(5,0,-1):
for x in range(1,i+1):
  print("*",end=" ")
print(" ")

==============================================================

===========================파이썬=============================

import turtle as t

win = t.Screen()
ub = t.Turtle()

win.setup(600,600)
angle = 119

win.bgcolor("black")
ub.color("yellow")
ub.speed(100)
a=["red","yellow","blue"]
x=0
i=0
while x < 1000:
   if x%4==1:ub.color("blue")
   elif x%4==2:ub.color("red")
   elif x%4==3:ub.color("green")
   else: ub.color("blue")
   # ub.color(a[i])
   # i=i+1
   # if(i==3):
   #     i=0
   # ub.left(angle)
   # x=x+2
win.exitonclick()

==============================================================

import turtle as t
import random
t.bgcolor("black")

lnt =10
gak = 89
t.speed(0)
c_l=["red",'blue',"green","yellow"]
while lnt<500:
    for i in range(4):
        t.color(c_l[random.randint(0,3)])
        t.fd(lnt)
        t.rt(gak)
        lnt+=5

==============================================================

#n각형
import turtle as t
def da(a):
    for i in range(a):
        t.fd(30)
        t.rt(360/a)
def main():
    n = int(input("어떤 정다각형을 그리시겠습니까?(숫자입력)"))
    da(n)

main()

==============================================================

#bmi계산기
def bmi(bkg, btall):
    return bkg//(btall*btall)
while True:
    kg = int(input("당신의 몸무게는?"))
    tall = float(input("당신의 키를 m단위로 입력하십시오"))

    h = bmi(kg, tall)
    print(h)

    if h<20:
        print("저체중입니다")
    elif 20<h<25:
        print("정상체중입니다")
    elif 25<h<30:
        print("경도비만입니다")
    else :
        print("비만입니다")

    dap = int(input("계속하시겠습니까?(yes=1, no=2)"))

    if dap == 1:
        print("알겠습니다")
    elif dap == 2 :
        print("감사합니다")
        break

    else:
        print("잘못 입력하셨습니다")

==============================================================

#n각형 컬러
import turtle as t
t=t.Turtle()
color_list=["violet","red","blue","brown","green",
            "pink","orange","black","gray"]
t.speed(5)
def poly(n,length):
    for i in range(n):
        t.fd(length)
        t.lt(360//n)

for i in range(18):
    t.color(color_list[i%9])
    t.lt(20)
    poly(6,50)

==============================================================

#n각형 다양하게그리기
import turtle as t
import random
t=t.Turtle()
color_list=["violet","red","blue","brown","green","pink","orange",
            "black","gray"]

def dodo(length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360//n)

for i in range(20):
    t.color(color_list[i%9])
    x=random.randint(-400,400)
    y=random.randint(-300,300)


    polygon=random.randint(3,6)
    size=random.randint(10,40)

    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    dodo(size,polygon)
    t.end_fill()

==============================================================

#함수 n각형
import turtle as t
a = int(input("한 변의 길이를 입력하십시오"))
b= int(input("도형의 이름을 숫자로 입력하십시오"))

t=t.Turtle()
def n_polygon(n, length):
    for i in range(n):
        t.fd(length)
        t.left(360//n)

for i in range(b):
    t.left(b)
    n_polygon(b,a)

==============================================================

#파이두
def pi(a,b):
    return a*a*b
def pii(a,b):
    return (a+a)*b

k=int(input("반지름의 길이를 입력하세요"))

g=3.14159265358979
u=pi(k,g)
s=pii(k,g)
print("반지름이",k, "인 원의 면적:",u)
print("반지름이",k,"인 원의 둘레:",s)

==============================================================

#미로
import turtle as t

def maze(x,y):
    for i in range(2):
        t.penup()
        if i == 1:
            t.goto(x+100,y+100)
        else :
            t.goto(x,y)
        t.pendown()
        t.fd(300)
        t.rt(90)
        t.fd(300)
        t.lt(90)
        t.fd(300)
def lit():
    t.lt(10)
    t.fd(10)
def rit():
    t.rt(10)
    t.fd(10)
s=t.Screen()
t.speed(5)

maze(-300,200)
s.onkey(lit,"Left")
s.onkey(rit,"Right")

t.penup()
t.goto(-300,250)
t.pendown()
s.listen()
s.mainloop()

==============================================================

#한붓그리기
import turtle as t

def drr(x,y):
    t.goto(x,y)

t.pensize(5)

s=t.Screen()
s.onscreenclick(drr)

==============================================================

#한붓그리기
import turtle as t

def drr(x,y):
    t.goto(x,y)

t.pensize(5)

s=t.Screen()
s.onscreenclick(drr)

==============================================================

#클릭
import turtle as t

n=int(input("몇각형을 그리시겠습니까?(숫자로입력)"))

def one(length):
    for i in range(n):
        t.fd(length)
        t.rt(360/n)
def draw(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.color("green")
    one(50)
    t.end_fill()


s= t.Screen()
s.onscreenclick(draw)

==============================================================

============================함수==============================

# 키보드로 거북이를 조종해서 그림 그리기
import turtle as t

def turn_right():                    # 오른쪽으로 이동하는 함수
    t.setheading(0)                  # t.seth(0)로 입력해도 됩니다.
    t.forward(10)                    # t.fd(10)로 입력해도 됩니다.

def turn_up():                       # 위로 이동하는 함수
    t.setheading(90)
    t.forward(10)

def turn_left():                    # 왼쪽으로 이동하는 함수
    t.setheading(180)
    t.forward(10)

def turn_down():                    # 아래로 이동하는 함수
    t.setheading(270)
    t.forward(10)

def blank():                        # 화면을 지우는 함수
    t.clear()

t.shape("turtle")                   # 거북이 모양을 사용합니다.
t.speed(0)                          # 거북이 속도를 가장 빠르게 지정합니다.
t.onkeypress(turn_right, "Right")   # [→]를 누르면 turn_right 함수를 실행합니다.
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(blank, "Escape")       # [Esc]를 누르면 blank 함수를 실행합니다.
t.listen()                          # 거북이 그래픽 창이 키보드 입력을 받습니다.

==============================================================

def add(a,b):
    return  a+b
def my(a,b):
    return  a-b
def gob(a,b):
    return  a*b
def na(a,b):
    if b==0:
        print("0으로는 나눌수 없습니다")
    else:                                       #10
        return a/b

def main():
    sa=" "
    a1=0
    b1=0
    result =0
    a1=int(input("첫번째 숫자를 입력하세요"))
    b1=int(input("두번째 숫자를 입력하세요"))
    sa=input("연산자를 입력하십시오")    #20

    if sa =="+":
        result =add(a1,b1)
    elif sa =="-":
        result =my(a1,b1)
    elif sa =="x":
        result =gob(a1,b1)
    elif sa =="/":
        result =na(a1,b1)
    else :                                          #30
        print("사칙연산이 아닙니다(+,-,x,/ 중 하나)")
    print(result)
main()

==============================================================

def gugu(dan):
    for i in range(1,10):
        a = print(dan, "*",i,"=",dan*i)

def main():
    for i in range(1,10):
        print("======================")
        gugu(i)

main()

==============================================================

def fact(n):
  if n == 1:
    return 1
  else:
    return n*fact(n-1)
n= int(input("정수를 입력하십시오"))
f = fact(n)
print(n,"!은",f,"이다")

==============================================================

============================집합==============================

s=set()
s={1,2,5}

s.add(11)
s.add(6)
s.remove(11)
s.discard(6)
print(s)

==============================================================

plant={'수성':91700000,'금성':41400000,'화성':78400000,'목성':628700000,'토성':1277400000,'천왕성':2750400000,'해왕성':4347400000}
a=input("어떤행성에 가시겠습니까?")
b=int(input("이동속도는?(km/h)"))
dis=plant[a]

time = dis / b

year = int(time)/(365*24)
month = int(time)%(365*24)/(30*24)
day = int(time)%(365*24)%(30*24)/24
hour = int(time)%(365*24)%(30*24)%24
print('이동시간:',time)
print(year,'년',month,'월',day,'일',hour,'시간')

==============================================================

award =[]
award.append({'이름':'팀버스너리','수상년도':2016,'국적':'영국','대표업적':'월드와이트 웹의 하이퍼 텍스트 시스템을 고안하여 개발'})
award.append({'이름':'리처드 해밍','수상년도':1968,'국적':'미국','대표업적':'오류 검출 부호 및 오류 정정 부호'})
award.append({'이름':'에프허르 데이크스트라','수상년도':1972,'국적':'네덜란드','대표업적':'프로그래밍 언어 연구,데이크스타 알고리즘'})
award.append({'이름':'더글러스 엥겔바트','수상년도':1997,'국적':'미국','대표업적':'월드와이트 웹의 하이퍼 텍스트 시스템을 고안하여 개발'})
award.append({'이름':'데니스 리치','수상년도':1983,'국적':'미국','대표업적':'유닉스 운영 체제개발, C언어 개발'})

for awards in award:
  print(awards)

print("수상자명단")
for awards in award:
  print(awards['이름'])

print()
print("수상자명단과 수상년도")
for awards in award:
  if awards['수상년도'] <=1990:
    print(awards['이름'],awards['수상년도'])

print()
print("수상국가")
nationality=set()
for awards in award:
  nationality.add(awards['국적'])
print(nationality)

==============================================================

items={"커피":7, "펜": 3, "종이컵":10, "우유":2, "콜라":4, "라면":9}
print("판매 전 재고", items)

sell=input("판매할 물건을 입력하십시오:")

if sell in items:
  items[sell]-=1
else:
  print("판매 제품이아닙니다")

print("판매 후 제고", items)

==============================================================

phone_book={'홍길동':'010-1234-5678','이순신':'010-7777-7777','김수이':'010-0984-7648'}
phone_book={"김수이"}
print(phone_book)

==============================================================

eng ={}
eng['one']='하나'
eng['two']='둘'
eng['three']='셋'
word = input("단어를 입력하십시오:")
print(eng[word])

==============================================================

phone_b={'홍길동':'010-1234-5678',
         '이순신':'010-7777-7777',
         '김수이':'010-0001-1000',
         '장영실':'010-0100-1234'}
for i in phone_b.keys():
  print(i)
for i in phone_b.values():
  print(i)

==============================================================

phone_book={'홍길동':'010-1234-5678',
         '이순신':'010-7777-7777',
         '김수이':'010-0001-1000',
         '장영실':'010-0100-1234'}
for k,v in phone_book.items():
  print('{}의 전화번호는 {}입니다'.format(k,v))

==============================================================

menu=0
items_it={"커피":7, "펜": 3, "종이컵":10, "우유":2, "콜라":4, "라면":9}
while menu!=9:
  print("현재수량")
  print(items_it)
  print("-------------------")
  print("1.추가할 물건 선택")
  print("2.삭제할 물건 선택")
  print("3.물건 이름 검색")
  print("4.물건 판매")
  print("5.물건 수입")
  print("9.종료")
  print("-------------------")
  menu = int(input("메뉴를 선택하십시오"))
  if menu == 1:
    nameadd=input("추가할 물건을 입력하십시오")
    add=input("추가할 음식의 수량을 입력하십시오")
    items_it[nameadd]=add
    print(items_it)
  elif menu == 2:
    nameby=input("삭제할 물건을 입력하십시오")
    del items_it[nameby]
    print(items_it)
  elif menu == 3:
    item=input("물건의 이름을 입력하십시오")
    print(items_it[item])
  elif menu == 4:
    panda=input("판매할 물건을 입력하십시오")
    if panda in items_it:
      items_it[panda]-=1
      print(items_it)
    else:
      print("없는 물건입니다")
  elif menu == 5:
    plus = input("수입할 물건을 입력하십시오")
    if plus in items_it:
      items_it[plus]+=1
      print(items_it)
    else:
      print("없는 물건입니다")
  elif menu == 9:
    print("종료합니다")
    break
  else:
    print("발견되지 않은 숫자입니다. 다시 해주십시오")

==============================================================

menu = 0
fri = []
while menu !=9:
  print("-------------------")
  print("1.친구 리스트 출력")
  print("2.친구추가")
  print("3.친구삭제")
  print("4.이름변경")
  print("9.종료")
  print("-------------------")
  menu = int(input("메뉴를 선택하십시오"))
  if menu == 1:
    print(fri)
  elif menu == 2:
    name = input("이름을 입력하십시오")
    fri.append(name)
  elif menu == 3:
    del_name = input("삭제하고 싶은 이름을 입력하십시오")
    if del_name in fri:
      fri.remove(del_name)
    else:
      print("이름이 발견되지 않음")
  elif menu == 4:
    old_name = input("변경할 이름을 입력하십시오")
    if old_name in fri:
      index = fri.index(old_name)
      new_name = input("새로운 이름을 입력하십시오")
      fri[index] = new_name
  if menu == 9:
    print("종료합니다")
    break

==============================================================

size = 0
xxl= 0
xl=0
l=0
m=0
xs=0
s=0

shirt_size=["XXL", "XL", "XS", "L", "L", "S"]
for i in range(len(shirt_size)):
#for i in shirt_size:
  if shirt_size[i] == "XS":
    xs+=1
  elif shirt_size[i] =="XL":
    xl+=1
  elif shirt_size[i]== "XXL":
    xxl+=1
  elif shirt_size[i]=="L":
    l+=1
  elif shirt_size[i]=="S":
    s+=1
  elif shirt_size[i]=="M":
    m+=1
print("|shirt_size                                          |return|")
print("|------------------|---------------|-----------------|------|")
print("|[XXL XL XS L M S] |[",xxl, xl, xs, l, m, s,"]|")

==============================================================

def func_a(month, day):
  month_list=[31,28,31,30,31,30,31,31,30,31,30,31]
  total=0
  for i in range(month-1):
    total +=month_list[i]
  total+=day
  return total

def solution(start_month, start_day, end_month, end_day):
  start_total= func_a(start_month, start_day)
  end_total=func_a(end_month, start_day)
  return end_total - start_total

start_month=1
start_day=2
end_month=2
end_day=2
ret= solution(start_month, start_day, end_month, end_day)

print(ret)

==============================================================

grade=input("등급 s v g 중 고르세요")
price=int(input("가격은 얼마입니까"))
if grade== "s":
  price-=price*0.05
elif grade =="g":
  price-=price*0.1
elif grade =="v":
  price-=price*0.15
print(price)

==============================================================

o=0
e=0
t=0
list=[1,1,2,3,3,2,3,2,3,3,3,2]
for q in range(len(list)):
  if list[q] == 1:
    o+=1
  elif list[q] == 2:
    e+=1
  elif list[q] == 3:
    t+=1
print(o, e, t)
if o<e<t:
  print(t/o)
elif e<o<t:
  print(t/e)
elif o<t<e:
  print(e/o)
elif t<o<e:
  print(e/t)
elif t<e<o:
  print(o/t)
elif e<t<o:
  print(o/e)

==============================================================

number = 40
count =0
for i in range(number):
  for a in str(i):
    if '3' in a or '6' in a or '9' in a:
      count+=1
      print(i,end=' ')
print('\n',count)

==============================================================

list1 = [4, 5 ,6]
list2 = [1, 2, 3]
print(list1 > list2)

==============================================================

import time
size = 50000

start_time = time.time()
mylist = []
for i in range(size):
  mylist = mylist + [i*i]
print("수행시간=",time.time()-start_time)

start_time = time.time()
mylist = []
for i in range(size):
  mylist.append(i * i)
print("수행시간=", time.time() - start_time)

==============================================================

list = [1, 2, 3, 4, 5, 6, 7, 8]
list[0:3] = ['red', 'white', 'blue', 'green']
list

==============================================================

import random
test=[]
for i in range(10):
    test.append(random.randint(1,100))
print(test)
test[::-1]
s= "good morning"
s[0:4]
list=[10, 20, 30, 40, 50, 60, 70, 80, 90]
a = input("입력할 값의 개수 :")
list[1]

==============================================================

import random
test=[]
for i in range(10):
    test.append(random.randint(1,100))
test

==============================================================

import random
test=[]
for i in range(10):
    test.append(random.randint(1,50))

#별찍기
for i in range(len(test)):
  print(test[i],"*"*test[i])

==============================================================

oddnumber=[1,3,5,7.9]
cafes=['star','bene','yoger','friends']
A=[1,5,'A','CC','b']
listInit=[[1,3,5,6,7],cafes,oddnumber,1,3,'Abc']
print(oddnumber)
print(cafes)
print(A)
print(listInit)

==============================================================

oddnumber=[1,3,5,7.9]
cafes=['star','bene','yoger','friends']
A=[1,5,'A','CC','b']
listInit=[[1,3,5,6,7],cafes,oddnumber,1,3,'Abc']

a=oddnumber[1:5]
b=cafes[1:]
c=A[:3]
d=listInit[0][1:4]

print(a)
print(b)
print(c)
print(d)

==============================================================

my_list=['a',1,2,3,'b',['apple','banana'],4]
a= my_list[3:4]
my_list[2]='hello'
b= my_list[:6]
c=my_list[2][1]

print(a)
print(my_list)
print(b)
print(c)

==============================================================

even_numbers=[2,4,6,8,10]
odd_numbers=[1,3,5,7,9]
numbers= even_numbers+odd_numbers
numbers[4]=100
print(numbers)
numbers[2]='hello'
print(numbers)
numbers[0]=numbers[9]
print(numbers)
numbers[8]=['a','b','c']

==============================================================

even_numbers=[2,4,6,8,10]
odd_numbers=[1,3,5,7,9]
numbers= even_numbers+odd_numbers

a="goorm"

del numbers[4]
print(numbers)
del numbers[:5]
print(numbers)
print(a)
del a

==============================================================

even_numbers=[2,4,6,8,10]
odd_numbers=[1,3,5,7,9]

print(even_numbers, odd_numbers)

even_numbers.append(10)
odd_numbers.append(9)
print(even_numbers, odd_numbers)

numbers=even_numbers+odd_numbers
print(numbers)
numbers.sort()
print("sort=>", numbers)

numbers.reverse()
print("reverse=>",numbers)
numbers.insert(3,[11,12,13])
print("insert=>",numbers)
numbers.remove(9)
print("remove=>",numbers)
print(numbers.pop())
print("pop",numbers)

numbers.extend(['a','b','c'])
print("extend=>",numbers)
numbers.append(['a','b','c'])
print("append=>",numbers)

==============================================================

list1=[1,2,3,4,3]
list1.reverse()
print(list1)

==============================================================

a=[1,9,2,3,4,5,7]
number=a
number.sort()
print(number)
number.remove(9)
print(number)
number.insert(5,6)
print(number)
number.append(8)
print(number)
number.reverse()
print(number)

==============================================================

num=1
sum=0

while num<=10:
  sum +=num
  num+=1
print(sum)

==============================================================

evennumbers=[]
num=2

while num<=30:
  evennumbers.append(num)
  num+=2
print(evennumbers)

==============================================================

i = 0
while i<=9:
  i+=1
  print("개구리",i,"마리")

==============================================================

my_list=[3,2,1,4,5,9,7]
my_list.sort()
print(my_list)
my_list.remove(9)
print(my_list)
my_list.insert(4,10)
print(my_list)
my_list.append(8)
print(my_list)
my_list.append("goorm")
print(my_list)
my_list.reverse()
print(my_list)

==============================================================

list2=my_list[:5]
print(list2)
list2.extend(['c','o','d','e'])
print(list2)
list2.extend(['cow','cat','dog'])
print(list2)
list2.remove(10)
print(list2)
list2.pop()
print(list2)

==============================================================

my_dict={'model':'iphonexs',
         'manufacturer':'apple',
         'year':'2020'}
print(my_dict)
del my_dict['year']
print(my_dict)
my_dict['fruits']=['apple','orange','melon']
print(my_dict)
my_dict['animal']={'cow':'소','cat':'고양이'}
print(my_dict)
print(my_dict.keys())
print(my_dict.values())

==============================================================

===========================클래스=============================

class Calculator:
  def __init__(self):
    self.result = 0
  def add(self,num):
    self.result+=num
    return self.result
  def min(self, num):
    self.result-=num
    return self.result

cal1 = Calculator()
cal2 = Calculator()
print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))
print(cal1.min(4))
print(cal2.min(6))

==============================================================

class Calculator:
  def setdata(self, first, second):
    self.first = first
    self.second = second
print(self.first)

==============================================================

class Fourcal:
  def __init__(self, first, second):
    #인스턴스 변수 선언
    self.first=first
    self.second=second
  def setdata(self, first, second):
    self.first=first
    self.second=second
  def add(self):
    result = self.first+self.second
    return result
  def min(self):
    result = self.first-self.second
    return result
  def mul(self):
    result = self.first*self.second
    return result
  def nan(self):
    result = self.first//self.second
    return result

==============================================================

print(cal.add())
print(cal.min())
print(cal.mul())
print(cal.nan())

==============================================================

print("계산기 입니다!")
a=int(input("첫번째 숫자를 입력해주십시오"))
b=int(input("두번째 숫자를 입력해주십시오"))
print("==============(덧셈은 1, 뺄셈은 2, 곱셈은 3, 나눗셈은 4를 입력해주세요.)===============")
menu=int(input("원하는 사칙연산을 입력해주십시오"))
cal = Fourcal(a,b)
if menu == 1:
  print(cal.add())
if menu == 2:
  print(cal.min())
if menu == 3:
  print(cal.mul())
if menu == 4:
  print(cal.nan())

==============================================================

class MoreFourCal(Fourcal):
  def pow(self):
    result = self.first ** self.second
    return result

==============================================================

mcal = MoreFourCal(4, 2)
mcal.add()
mcal.pow()
m=Fourcal(4,0)

==============================================================

class SafeFourcal(Fourcal):
  def nan(self):
    if self.second == 0:
      return 0
    else :
      return self.first / self.second

==============================================================

a = SafeFourcal(4, 0)
a.nan()

==============================================================

class Dog():
  def __init__(self,name):
    self.name = name
  def bark(self):
    print("멍")

==============================================================

class Cat():
  def __init__(self,name,age):
    self.name= name
    self.age=age
  def __str__(self):
    msg=self.name+"의 나이는 "+str(self.age)+"살 입니다."
    return msg

==============================================================

missy=Cat('Missy',3)
lucky=Cat('Lucky',5)
print(missy)
print(lucky)

==============================================================

class Calulator:
  def __init__(self):
    self.value = 0

  def add(self, val):
    self.value += val

==============================================================

class UpgradeCalulator(Calulator):
  def minus(self,val):
    self.value -=val

cal=UpgradeCalulator()
cal.add(10)
cal.minus(7)

print(cal.value)

==============================================================

#colab
from google.colab import files
uploaded = files.upload()

#모두
import csv
f = open("extremum_20230119104639.csv",'r',encoding=('cp949'))
data = csv.reader(f,delimiter=',')

for row in data:
  print(row)

f.close()

==============================================================

#헤더만
import csv
f = open("extremum_20230119104639.csv",'r',encoding=('cp949'))
data = csv.reader(f,delimiter=',')

header = next(data)

for row in data:
  print(row)
  
  row[4] = float(row[4])
  row[-2] = float(row[-2])


f.close()

==============================================================

import csv
f = open("extremum_20230118104714.csv",'r',encoding=('cp949'))
data = csv.reader(f,delimiter='.')

header = next(data)

max_temp = -999
mat_date = ''
for row in data:
  if row[5] == '':
    row[5] = -999
  row[5] = float(row[5])
  if mat_temp < row[5]:
    max_date = row[6]
    mat_temp = row[5]
  f.close()
  import csv
print("기상 관측 아래 서울의 최고 기온이 가장 높았던 날은 %s로 %.2f였습니다",mat_date, max_temp)

==============================================================

import csv
f = open("extremum_20230119101035.csv",'r',encoding=('cp949'))
data = csv.reader(f,delimiter='.')

header = next(data)

result = []

for row in data:
  if row[5] != '':
    result.append(float(row[5]))
print(result)

import matplotlib.pyplot as plt
plt.plot(result,'r')

plt.title('plotting')
plt.plot([1,2,3,4],[10,20,30,40], label='acs')
plt.plot([1,2,3,4],[40,30,20,10], label='dcse')
plt.legend()
plt.show()

==============================================================

import matplotlib.pyplot as plt
plt.plot([1,2,3,4],[10,20,30,40], label='asc')
plt.plot([1,2,3,4],[40,30,20,10], label='decs')
plt.show()

==============================================================

t = ["법사","파이썬 스쿨 선생님",77,80,["타임머신","순간이동","투명변신"]]
print("인덱스1 :",t[0])
print("인덱스2 :",t[3])
print("인덱스3 :",t[-1])

t.append(100)
t.append("건강")
print(t)

==============================================================

m = ['장미','벌침','이슬']
p = ['꿀잠','비행']

if len(m) >= 3 and '장미' in m:
  print('러브 포션 완성')
  p.append('러브')

else:
  print("정체 모를 포션 완성")

for i in p:
  print("포션 보유중중")

==============================================================

import requests
from bs4 import BeautifulSoup

url = 'https://weather.naver.com/'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
temperature_element = soup.find('strong', class_='current')
print("Current Temperature:", temperature_element)
