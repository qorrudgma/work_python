# utf-8 세계표준 문자셋

# f = open("new_file.txt","w",encoding="utf-8")      #파일을 생성하고 내용 입력
# names = ["홍지수","안지영","김연수","김예린","한정연"]

# for name in names:
#     f.write(name+"\n")

# print("파일작성 완료")
# f.close()

#====================================

# f = open("new_file.txt","a",encoding="utf-8")   #기존파일에 두명을 추가
# names = ["손영민","황현준"]

# for name in names:
#     f.write(name+"\n")

# print("파일작성 완료")
# f.close()

#====================================

# f = open("new_file.txt", "r",encoding="utf-8")
# # lines = f.readline()             #파일에서 한줄을 읽어옴
# lines = f.readlines()              #파일에서 모든 줄을 읽어옴

# for line in lines:
#     temp=line.replace("\n","")
#     print(temp)

# # print(lines)
# print("파일 읽기 완료")
# f.close()

#====================================

# # with open("scores.txt", "r", encoding="utf-8") as f:   #별칭 f로 하겠다(파일도 자동으로 닫힘)
# f = open("scores.txt", "r", encoding="utf-8")   #별칭 f로 하겠다(파일도 자동으로 닫힘)
# lines=f.readlines()

# for line in lines:
#     data=line.split()
#     i=0
#     sum=0
#     while i<len(data):
#         if i==0:
#             print(data[i], end=" : ")
#         else:
#             sum+=int(data[i])
#         i+=1
#     avg=sum/(len(data)-1)
#     print("%.1f점" %avg)

# print("파일읽기완료!")

# f.close()

#====================================

# import os

# # if os.path.exists("scores2.txt"):  #파일이 있으면 삭제 없으면 아래 출력
# #     os.remove("scores2.txt")
# if os.path.exists("scores2"):  #폴더가 있으면 삭제 없으면 아래 출력
#     os.rmdir("scores")
# else:
#     print("파일이 존재하지 않음!")











#====================================

r = open("test.txt", "r", encoding="utf-8")   #별칭 f로 하겠다(파일도 자동으로 닫힘)
lines_r=r.readlines()

# a = open("test.txt", "a", encoding="utf-8")
# lines_a=r.write()

# append를 사용하지말고 그냥 인풋 값을들 나열하고 그대로 텍스트에다가 넣으면 되지않을까?
# 추가를하고 그 것들을 반복문으로 돌리자 if를 사용해서 특정 단어나 행동을 취하면 멈추게하기




for line in lines_r:
    data=line.split()
    i=0
    sum=0
    while i<len(data):
        if i==0:
            print(data[i], end=" : ")
        else:
            sum+=int(data[i])
        i+=1
    avg=sum/(len(data)-1)
    print("%.1f점" %avg)

print("파일읽기완료!")
r.close()

# 날씨 데이터 오픈api가져올수있으니까 그거 가져와서 그걸로 내가 원하는 날짜를 고르면 그날의 기온들 알게하기



score=""

while score:
    name = input("이름 입력: ")
    score1=int(input("점수1 입력: "))
    score2=int(input("점수2 입력: "))
    score3=int(input("점수3 입력: "))
    score4=int(input("점수4 입력: "))
    score5=int(input("점수5 입력: "))





# input1=input("이름 입력: ")
# input2=int(input("점수1 입력: "))
# input3=int(input("점수2 입력: "))
# input4=int(input("점수3 입력: "))
# input5=int(input("점수4 입력: "))
# input6=int(input("점수5 입력: "))
# score=[]
# j=0
# while j<7:
#     score.append("input%d"%j)
#     j+=1

# for name in name:
#      f.write(name+"\n")