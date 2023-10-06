A = {1,2,3}
B = {1,3,4}
print(A|B) #|로 합집합
print(A&B) #&로 교집합
print(len(A)) #len으로 원소 개수

A = set("한파,눈,예보,일부,비".split(","))
B = set("눈,예보,퇴근길,조심".split(","))
C = set("비,예보,일부,눈,그치다,한파".split(","))
print(A|B|C)


listU = list(U)
print(listU)

def Vec(X):
    result = []
    for t in listU:
        if t in X:
            result.append(1)
        else:
            result.append(0)
    return np.array(result)

print(Vec(A))
print(Vec(B))
print(Vec(C))




import numpy as np

#한파,눈,예보,일부,비,퇴근길,조심,그치다
VA = np.array([1,1,2,1,1,0,0,0])
VB = np.array([0,2,1,0,0,1,1,0])
VC = np.array([1,1,1,1,3,0,0,1])

print(VA)
print(VA)


def Bin(X):
  result = []
  for i in X:
    if i !=0:
      result.append(1)
    else:
      result.append(0)
  return(np.array(result))

#TF
print(VA+VB+VC)

#DF/n
print(Bin(VA)+Bin(VB)+Bin(VC)/3)

#IDF
IDF = print(1/((Bin(VA)+Bin(VB)+Bin(VC))/3))
print(IDF)
#TF*IDF
print(VA*IDF)



import numpy as np

a=[1,2,3,4]
b=[[1,2,3,4],
   [1,2,2,1]]

A = np.matrix([[1,2],
               [0,1]])
B = np.matrix([[1,2],
               [3,4]])
C = np.matrix([[3,2],
               [-4,5]])
D = np.matrix([[2],
               [1]])
I = np.matrix([[1,0],
               [0,1]])

print(A)
print(A*I)
print(I*D)

import numpy as np

T = np.matrix([[0,1,0],
               [0,0,1],
               [0,0,0]])
A = np.matrix([[0,0,0],
               [0,255,0],
               [0,0,0]])

print(A*T)
print(T*A)


import numpy as np

def perc(X,W,d):
  X = np.array(X)
  W = np.array(W)
  S = np.dot(X,W) #dot연산 : 내적, 선형결합
  if S>=d:
    return(1)
  else:
    return(0)

def perc_and(X):
  return(perc(X,[5,5],6))
def perc_or(X):
  return(perc(X,[5,5],4))
def perc_nand(X):
  return(1-perc_and(X))
def perc_xor(X):
  return(perc_and([perc_nand(X),perc_or(X)]))



for x in range(2):
  for y in range(2):
    print(perc_xor([x,y]))

import numpy as np

A = np.array([[0,1,1,1,0],
             [1,0,0,0,1],
             [1,0,0,1,1],
             [1,0,1,0,1],
             [1,1,0,0,1],
             [1,0,0,0,1],
             [0,1,1,1,0]])

B = np.array([[0,1,1,1,0],
             [1,0,0,0,1],
             [1,0,0,0,1],
             [0,1,1,1,0],
             [1,0,0,0,1],
             [1,0,0,0,1],
             [0,1,1,1,0]])

C = np.array([[0,1,1,1,0],
             [1,0,0,0,1],
             [1,0,0,0,1],
             [0,0,0,0,0],
             [1,0,0,0,1],
             [1,0,0,0,1],
             [0,1,1,1,0]])

D = np.array([[0, 1, 0, 1, 0],
              [1, 0, 1, 0, 1],
              [0, 1, 0, 1, 0],
              [1, 0, 1, 0, 1],
              [1, 0, 0, 0, 1],
              [0, 1, 0, 1, 0]])



#sum은 모든 성분의 합
np.sum(D)

#abs는 모든성분의 절댓값
np.abs(-D)


def H(X,Y):
  return(np.abs(np.sum(X-Y)))

def P(X,Y):
  return(np.sum(X*Y)/np.sum(X))

for X, i in enumerate([A,B,C]):
  #psrint(H(X,D),"해밍{}번째".format(i))
  print(P(X,C),"퍼셉트론{}번째".format(i))

import pandas as pd
datalist = [["Weat","S,S,C,R,R,R,C,S,S,R,S,C,C,R".split(",")],
            ["Temp","H,H,H,N,C,C,C,H,C,N,N,N,H,B".split(",")],
            ["Exer",[0,0,1,1,1,0,1,0,1,1,1,1,1,0]]]

df = pd.DataFrame.from_dict(dict(datalist))
#df.groupby("Exer").count()
#df.groupby("Weat").count()
#df.groupby(["Temp","Exer"]).count()
#판다스를 사용해보았다


