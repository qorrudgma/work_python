# for i in range(5):      #0~4까지 출력 (i값에 0이 기본으로 들어감)
#     print("안녕하세요")
# print("===============")

# for i in range(1, 5):      #1~4 까지 출력 (두개 적으면 초기값과 끝값+1을 적는다)
#     print("안녕하세요")
# print("===============")

# for i in range(1, 5, 2):      #1~4 까지인데 2씩증가라서 1이랑 3만 있어서 2개 출력 (세개 적으면 초기값과 끝값+1 증가값을 적는다)
#     print("안녕하세요")
# print("===============")

# sum=0
# for i in range(1, 11):
#     sum+=i
#     print("i의 값:%d=> 합계:%d"%(i,sum))
# print("===============")

# for i in range(1, 11):
#     print(i, end=" ")

# for i in range(9, 0, -1):
#     print(i, end=" ")
# print("===============")


# sum=0
# for i in range(100,201,5):
#     sum+=i
# print("5의 배수의 합계:%d" %sum)
    #위와같음
# for i in range(100,201):
#     if i%5==0:
#         sum+=i
# print("5의 배수의 합계:%d" %sum)

#range 없이도 반복문 가능
# word = input("영어 문장을 입력하세요:")
# for x in word:        #문자를 하나씩 출력
#     print(x)

# phone = input("하이픈(-)을 포함한 휴대폰 번호를 입력하세요:")
# for x in phone:
#     if x!="-":          #빼고 싶은 문자 제외
#         print(x, end="")

# print("-" * 15)
# print(" 섭씨  화씨")

# for c in range(-20,31,5):
#     f = c * 9.0/5.0+32.0
#     print("%4d %5.0f"%(c,f))     #d는 정수라 소숫점 안적음 f는 소숫점까지 생각해야함
# print("-" * 15)

# for a in range(2,10):
#     for b in range(1,10):
#         print("%d X %d = %2d"%(a,b,a*b),end="   ")
#     print()
#     print("-"*115)    #이거 가로로 출력되는데 세로로 하는 방법이 있을까?

for i in range(1,1001):
    print(i)
    if i==10:
        break