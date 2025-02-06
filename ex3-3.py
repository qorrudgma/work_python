score = int(input("점수는? "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("등급:",grade)    #들여쓰기가 달라 if문 끝나고 실행이 된다