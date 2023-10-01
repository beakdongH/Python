def mysubstr(str_input, start, count):
    return str_input[start:start+count]
def yo():
    str0 = input()
    start0,count0 = map(int, input().split())

    re = mysubstr(str0, start0, count0)
    print(re)

if __name__ == "__main__":
    yo()
