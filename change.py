price=3000
num=3
pay=10000

change=pay-price*num
# print(change) #오류
# print("거스름돈 --> 원" % change) #오류
print("거스름돈 --> %d원" %change) #d 정수
print("거스름돈 --> %f원" %change) #f 실수