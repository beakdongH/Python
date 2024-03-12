class Parent:
    num = 0
    # 생성자
    def __init__(self,num) -> None:
        self.num = num
        print("constructor of the parent class was called")
class Child(Parent):
    # 생성자
    def __init__(self, num) -> None:
        super().__init__(num)
        print("constructor of the child class was called")

    def displayValue(self):
            print("num :",self.num)

cd = Child(20)
cd.displayValue()