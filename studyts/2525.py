h,m = map(int,input().split())
a = int(input())

if a+m<60:
  print(h,a+m)
else:
  plus_h = (a+m)//60
  plus_m = (a+m)-(60*plus_h)
  hour = plus_h+h
  if hour>=24:
    print(hour-24,plus_m)
  else:
    print(hour, plus_m)

  
