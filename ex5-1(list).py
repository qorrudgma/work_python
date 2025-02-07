# list1=[3,15,-12.5,"사과", "딸기"]
# print(list1)

# list2=list(range(10))   #0~9
# list2=list(range(1,10))   #1~9
# list2=list(range(1,21,2))
# print(list2)

#===============================================================

color = ["빨강","주황","노랑","초록","파랑","남색","보라"]
# print(color[0])
# print(color[2:6])

# for c in color:
#     # print(c)
#     print("나는 %s을 좋아한다." %c)

# n = len(color)
# for i in range(0,n):
#     print("나는 %s을 좋아한다." %color[i])

# i=0
# while i<len(color):
#     print(i,":",color[i])
#     i+=1

# print(color)
# print(color[1])
# color[1]="황금색"
# print(color)
# print(color[1])

print(color)
color.append("실버")      #마지막에 주어진 값 추가
print(color)

#==============================================================

# scores = []

# while True:
#     score = int(input("성적을 입력하세요(종료:-1): "))  #문자 숫자 비교하면 무한 루프
#     if score == -1:
#         break
#     else:
#         scores.append(score)
# print(scores)

# fruits=["apple","orange","banana","cherry"]
# print(fruits)
# fruits.insert(1,"melon")
# print(fruits)
# fruits.insert(2,"strowberry")
# print(fruits)

# number=[5,20,13,7,8,22,7,17]
# print(number)
# idx = number.index(7)
# print(idx)

# member=["홍길동",20,"경기도 김포시","h@naver.com","010-1234-5678"]
# print(member)
# member.remove(20)
# print(member)

# data=[10,20,30,40,50,60,70,80]
# print(data)
# x=data.pop(2) #값이 없으면 마지막 값을 잘라냄
# print(x)
# print(data)

# data=[10,20,30,40,50,60,70,80]
# print(data)
# data.clear()
# print(data)

# person1=["kim",20,"kim@naver.com"]
# person2=["lee",30,"lee@naver.com"]
# person=person1+person2
# print(person)

# scores=[80,90,85,95,100]
# sm=sum(scores)
# avg=sm/len(scores)
# print("합계 : ",sm)
# print("평균 : ",avg)

# data=[80,90,85,95,100]
# print(data)
# data.reverse()
# print(data)

# fruits=["apple","banana","orange"]
# print(fruits)
# x=fruits.copy()
# print(x)

# data=[12,8,15,32,-3,-20,15,34,6]
# print(data)
# data.sort()
# print(data)
# data.sort(reverse=True)  #data.reverse()이거랑 같음
# print(data)

# string1="Python is fun!"
# print(string1)
# x=string1.find("fun")
# print(x)

# string1="사과는 맛있다. 나는 사과를 제일 좋아한다."
# x=string1.replace("사과","딸기")
# print(x)

# phone="010-1234-5678"
# print(phone)
# rephone=phone.replace("-","")
# print(rephone)

# hello="have a nice day"
# print(hello)
# list1=hello.split(" ")      #주어진 문자를 기준으로
# print(list1)
# print(type(list1))      #타입이 뭔지 구한다.

# for i in range(0,len(list1)):
#     print("list1[%d] : %s" %(i,list1[i]))

# names=["황예린","홍지수","안지영"]
# print(names)
# x="/".join(names)
# print(x)

# phone1=["010","1234","5678"]
# print(phone1)
# phone2="-".join(phone1)
# print(phone2)

# phone_list1=["010-1111-4512","010-2222-1234","010-3333-5678"]
# print(phone_list1)
# phone_list2=[]
# for number in phone_list1:
#     # print(number)
#     x=number.replace("-","")
#     phone_list2.append(x)
# print(phone_list2)

# sentences=["aaa bb","cc d","e f"]

# for sentence in sentences:
#     x=sentence.replace(" ","_")
#     print(x)

# number=[[10,20,30],[40,50,60,70,80,90]]

# print(number[0])
# print(number[0][0])
# print(number[0][1])
# print(number[1][3])