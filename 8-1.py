class Space:
    def hight(self,b, h):
        self.b=b
        self.h=h
        print("삼각형의 면적:",(self.b*self.h)/2)
h1=int(input("삼각형 밑변의 길이를 입력하세요: "))
b1=int(input("높이를 입력하세요: "))
x=Space(h1,b1)

x.hight()