def lineup(count,a):
    for i in range(0,count):
        num=1
        for j in range(0,count):
            if(a[i]<a[j]):
                num=num+1

        print(a[i],num)



if __name__=="__main__":
    count = int(input())
    n = list(map(int, input().split(" ")))
    lineup(count,n)

