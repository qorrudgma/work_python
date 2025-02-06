a = int(input("책 값은?"))
b = int(input("할인율은?"))
c = int(input("배송료는?"))

d = a-(a*(b/100))+c

print("================")
print("책 값 : %d원" %a)
print("할인율 : %d" %b)
print("배송료 : %d원" %c)
print("결제 금액 : %d원" %d)