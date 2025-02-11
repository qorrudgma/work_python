class Ladder:
    def __init__(self,a,b,h):
        self.a=a
        self.b=b
        self.h=h
    def area(self):
        return (self.a+self.b)/2*self.h
    
w1 =int(input("밑변: "))
w2 =int(input("윗변: "))
h1 =int(input("높이: "))

ladder1=Ladder(w1,w2,h1)
print("넓이: %.2f" %ladder1.area())