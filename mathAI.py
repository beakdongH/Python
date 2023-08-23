A = {1,2,3}
B = {1,3,4}
print(A|B) #|로 합집합
print(A&B) #&로 교집합
print(len(A)) #len으로 원소 개수

A = set("한파,눈,예보,일부,비".split(","))
B = set("눈,예보,퇴근길,조심".split(","))
C = set("비,예보,일부,눈,그치다,한파".split(","))
print(A|B|C)

import numpy as np
listA = "한파,눈,예보,일부,비".split(",")
listB = "눈,예보,퇴근길,조심".split(",")
listC = "비,예보,일부,눈,그치다,한파".split(",")

A = set(listA)
B = set(listB)
C = set(listC)
U = A|B|C

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
