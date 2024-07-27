def list_sum(n):
    value = n
    sum = 0
    while True:
        if(value == 0):
            break
        sum = sum+(value%10)
        value = value//10
        print(sum,value)
    return sum

if __name__ == "__main__":
    i = int(input())
    while True:
        if(i<10):
            break
        i = list_sum(i)
    print(i)
