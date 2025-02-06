score = int(input("숫자를 입력하세요 :"))
p = ""

# if score > 10:
#     print("%d은(는) 10보다 크다" %score) 
# elif score < 10:
#     print("%d은(는) 10보다 크지 않다." %score) 
# else:
#     print("%d은(는) 10이다" %score) 


if score > 10:
    p = "보다 크다"
elif score < 10:
    p = "보다 크지 않다"
else:
    p = "이다"

print("%d은(는) 10%s" %(score,p)) 