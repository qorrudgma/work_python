# animals = ("토끼","거북이","사자","여우",)
# print(animals)

# animals[2]="호랑이"     #튜플에서는 내용을 바꾸거나 삭제를 할수없다.
# print(animals)
# print(animals[2])

# n=tuple(range(10,21))
# print(n)

# print("n[0]=",n[0])
# print("n[2:5]=",n[2:5])
# print("n[2:]=",n[2:])
# print("n[:5]=",n[:5])
# print("n[-2]=",n[-2])
# print("n[::-1]=",n[::-1])       #맨뒤에서 부터 맨앞까지 출력
# print("n[::-3]=",n[::-3])

# tup1=(10,20,30,40,50)

# for i in range(len(tup1)):
#     print(tup1[i])
#    #위아래가 같음
# for i in tup1:
#     print(i)

# tup2=(10,20)
# tup3=(30,40)
# tup4=tup2+tup3
# print(tup4)

admin_info=("admin","12345","webmaster@naver.com")

print("관리자 정보")
print("아이디:"+admin_info[0])
print("비밀번호:"+admin_info[1])
print("이메일일:"+admin_info[2])