score = int(input("주민번호 뒷자리 첫 번째 숫자를 입력해 주세요 :"))

if (score%2==1)&(1<=score<=4):
    g="남"
elif (score%2==0)&(1<=score<=4):
    g="여"
else:
    score = int(input("다시 확인하시고 주민번호 뒷자리 첫 번째 숫자를 입력해 주세요 :"))

#다시 하려하면 안된다 이게 else에서 다시 if로 가게하거나 뭔가 다시 뜨게 만들어보기
print("%s성입니다!" %g)