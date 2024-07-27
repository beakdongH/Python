import os
print(os.getcwd())

path='c:/Users/dongheun/Desktop/openCV/IO.py'
fp = open(path)
str = fp.read()
print(str,end=" ")
fp.close