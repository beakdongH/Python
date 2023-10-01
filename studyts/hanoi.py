def hanoi(n,a,b,c):
    if(n==1):
        print("Disk {} : {} to {}".format(n,a,c))
    else:
        hanoi(n-1,a,c,b)
        print("Disk {} : {} to {}".format(n, a, c))
        hanoi(n-1,b,a,c)

n=int(input())
hanoi(n,'A','B','C')
    