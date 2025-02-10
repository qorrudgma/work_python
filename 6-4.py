# 변수 지정 후 딕셔너리 재편성
score = dict([("국어", 0),("영어", 0),("수학", 0)])

kor = int(input("국어 성적을 입력해주세요 :"))
eng = int(input("영어 성적을 입력해주세요 :"))
math = int(input("수학 성적을 입력해주세요 :"))

score["국어"] = kor
score["영어"] = eng
score["수학"] = math
arr=["국어","영어","수학","미술","음악"]

course_sub = "-"

while course_sub :
    course_sub = input("추가할 과목을 입력해주세요(-1 입력시 종료) :")

    if course_sub == "-1":
        break
    elif arr.count(course_sub)==0:
        print("해당과목은 없습니다. 다시 입력해주세요")
        continue
    else:
        course_score = int(input("과목의 점수를 입력해주세요(-1 입력시 종료) :"))
    score[course_sub] = course_score



    # if course_sub == "-1":
    #     break
    # elif arr.count(course_sub)==0:
    #     print("해당과목은 없습니다. 다시 입력해주세요")
    #     continue
    # else:
    #     course_score = int(input("과목의 점수를 입력해주세요(-1 입력시 종료) :"))
    # score[course_sub] = course_score


    # if course_sub == "-1":
    #     break
    # else:
    #     course_score = int(input("과목의 점수를 입력해주세요(-1 입력시 종료) :"))
    # score[course_sub] = course_score
    
#==========================================================
    # if course_sub == "-1":
    #     del score["-1"]
    
sum = 0

for key in score:
    sum += score[key]

avg = sum / len(score)

print("과목 수 : %d"%len(score))
print("평균 점수 : %.1f" %avg)
print(score)




