score = input("등급을 입력해 주세요(~~~):")
grade = ""


if score.upper() == "A+":   #대소문자 아무거나 적어도 작동함
    grade = 4.5
elif score.upper() == "A":
    grade = 4.0
elif score.upper() == "B+":
    grade = 3.5
elif score.upper() == "B":
    grade = 3.0
elif score.upper() == "C+":
    grade = 2.5
elif score.upper() == "C":
    grade = 2.0
elif score.upper() == "D+":
    grade = 1.5
elif score.upper() == "D":
    grade = 1.0
elif score.upper() == "F":
    grade = 0
else:
    print("%s라는 등급은 없습니다."%score)
    score = input("등급을 다시 입력해 주세요(~~~):")

print("등급:",score,", 평점:",grade)
print("등급:%s, 평점:%d" %(score,grade))