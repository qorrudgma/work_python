score = int(input("월을 숫자로 입력하세요 :"))
p = ""


# if 3<=score<=5 :
#     p = "봄"
# elif 6<=score<=8:
#     p = "여름"
# elif 9<=score<=11:
#     p = "가을"
# elif (score==12)&(1<=score<=2):
#     p = "가을"
# else:
#     p = "없는계절"
#     print("1년은 1월 부터 12월까지 밖에 없습니다.")

# print("%d월은 %s입니다." %(score,p))


if 3<=score<=5 :
    p = "봄"
elif 6<=score<=8:
    p = "여름"
elif 9<=score<=11:
    p = "가을"
elif (score==12)&(1<=score<=2):
    p = "가을"
else:
    p = ""

if p == "":
    print("1년은 1월 부터 12월까지 밖에 없습니다.")
else:
    print("%d월은 %s입니다." %(score,p))

# 더 좋은 방법 찾아보기