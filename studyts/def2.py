# *(별하나)이면 리스트 **(별 두개)이면 딕셔너리이다.

def caffe(beverage,*argument,**keyword):
    print("Do you have any",beverage+"?")
    for arg in argument:
        print(arg)
    print("===============================")
    for kw in keyword:
        print(kw,":",keyword[kw])

caffe("coffee","It's yummy, sir","Would you try?",
      barista = "Jay Kim",
      client="BSSM",
      cup="Venti-Size")