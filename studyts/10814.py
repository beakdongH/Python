n = int(input())
lst =[]


for i in range(n):
    age, name = input().split()
    lst.append([int(age),name])

for i in sorted(lst,key=lambda b:b[0]):
    print(i[0],i[1])