a = int(input())
b = int(input())
c = int(input())

tot = a*b*c

result = [0]*10

while tot>0:
    cnt = tot%10
    result[cnt]+=1
    tot//=10

for i in range(len(result)):
    print(result[i])