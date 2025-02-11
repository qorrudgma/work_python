# #class생성 => 속성생성 => (함수생성) => 객체생성 => 메소드 호출

# class Person:       #사람이나 사물이 될수 있는 틀/판
#     name="김정연"       #객체안에 없었으면 변수지만 객체 안에있기에 속성임(클래스 속성)
#     # person1객체를 self가 받음
#     def hello(self):    #hello 메소드 호출될때 객체를 self가 받는다
#         # print("안녕하세요")
#         print(Person.name+"님 안녕하세요")

# person1 = Person()     #객체 생성 해야함
# person1.hello()     #메소드 호출

# Person.name="황서영"
# person1.hello()     #메소드 호출

#=====================================================

# class Cat:
#     kor_name="로키"
#     eng_name="rocky"
#     age=2

#     def sound(self):
#         print("야옹~")
#     def speed(self):
#         print("엄청 빠르다!")

# mycat = Cat()

# print("한글 이름:",mycat.kor_name)      #객체의 속성으로 출력
# print("영어 이름:",mycat.eng_name)
# print("나이:",mycat.age)

# mycat.sound()
# mycat.speed()

#=====================================================

# class Members:

#     def set_info(self, name):
#         self.name=name      #객체의 속성
#         print(name)
#         # print(self.name)

#     def show_info(self):
#         print("이름: ", self.name)

# member1 = Members()
# member1.set_info("홍지수")
# member1.show_info()

# member2 = Members()
# member2.set_info("안지영")
# member2.show_info()

#=====================================================

# class Members:
#     def __init__(self, name, age):      
#         # pass    #동작없이 다음 실행
#         self.name=name
#         self.age=age

#     def show_info(self):
#         print("이름:", self.name,"\n나이:", self.age)

# member1 = Members("황선영", 18)     #객체를 생성하면서 생성자 __init__(self, name, age)를 호출한다
# member1.show_info()

# member2 = Members("최종하", 32)
# member2.show_info()

#=====================================================

# class Student:
#     # pet=[]        #클래스 속성이라 아래에서 존이랑 샐리 두가지랑 공유
#     def __init__(self):     #객체 속성이라 아래에서 존이랑 샐리 두가지랑 따로다
#         self.pet=[]
    
#     def push_pet(self,x):
#         self.pet.append(x)

# john=Student()
# john.push_pet("고양이")
# print(john.pet)

# sally=Student()
# sally.push_pet("이구아나")
# sally.push_pet("도마뱀")
# sally.push_pet("뱀")
# print(sally.pet)
# # print(Student().pet)

#=====================================================

# class Members:
#     total=0

#     def __init__(self, name, phone):
#         self.name=name
#         self.phone=phone
#         # self.total+=1
#         Members.total+=1
#     def show_info(self):
#         print("이름: %s\n전화번호: %s"%(self.name, self.phone))

# m1=Members("홍성지","010-1234-5678")        #__init__있어서 여기다 적음 show_info에 name이있었으면 아래에다 적는다
# m2=Members("강동욱","010-2222-2222")
# m3=Members("신진서","010-3333-3333")

# m1.show_info()
# m2.show_info()
# m3.show_info()

# print("총 회원 수:",m1.total)
# print("총 회원 수:",m2.total)
# print("총 회원 수:",m3.total)

# print("총회원수:",Members.total)

#=====================================================

# 확실하게 다시 알기**********
# class Person:
#     def __init__(self, name):
#         self.name=name
#     def show_name(self):
#         print(self.name)
#     def show_age(self):
#         print(self.age)

# class Student(Person):      #Person클래스(부모)를 상속받는 Student클래스(자식)
#     # def __init__(self, name):
#     def __init__(self, name, age):
#         super().__init__(name)      #부모 클래스의 생성자를 호출한다
#         self.age=age

# x=Student("홍지수", 21)
# x.show_name()
# x.show_age()

#=====================================================

class Person:
    def __init__(self, name):
        self.name=name
    def show_name(self):
        print(self.name)

class Student(Person):
    def show_name(self):    #오버라이딩
        print("환영합니다!")
        print(self.name+"님 반갑습니다.")

x=Student("홍지수")
x.show_name()       #자식의 메소드 호출









#=====================================================

# class Members:
#     def __init__(self, name, age):      
#         # pass    #동작없이 다음 실행
#         self.name=name
#         self.age=age

#     def show_info(self):
#         print("*"*30)
#         print("이름:", self.name,"\n나이:", self.age)



# member=dict()


# n=input("이름입력: ")
# a=int(input("나이입력: "))

# member1 = Members(n, a)
# member1.show_info()