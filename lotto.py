import random

# 번호를 랜덤으로 생성할껀지 아니면 내가 넣어둘건지 정하고 할수있게 만들기
# 

with open("lotto.txt", "r", encoding="utf-8") as win:
    numbers = win.readline()
    winning_numbers=[]
    for win_number in numbers.split():
        winning_numbers.append(int(win_number))

# 구매자로부터 로또 구매 금액 입력받기
def get_purchase_amount():
    while True:
        try:
            amount = int(input("구매할 금액을 입력하세요(1세트 = 1,000원):"))
            if amount < 1000 or amount % 1000 != 0:
                # raise: 에러를 강제로 발생시킨다   raise 대신 return이나 그런걸 써서 에러로 가능한가
                raise ValueError
            return amount // 1000   # amount / 5000를 사용하면 실수형이되버려서 n.0이라 몫만 반환환
        except ValueError:
            print("잘못된 입력입니다. 1,000원 단위로 입력하세요.")

# 구매자로부터 로또 타입 입력받기기
def lotto_type():
    type=input("'수동/자동'을 선택하여 입력하세요:")
    if type=="수동":
        user_lotto_numbers(set_count)
    elif type=="자동":
        user_lotto_numbers_auto(set_count)
    else:
        print("'수동/자동'을 다시 선택하세요.")

# 구매자로부터 set_count 개수만큼 로또 번호 입력받기
def user_lotto_numbers(set_count):
    user_numbers = []
    print("총 %d세트의 로또 번호를 입력하세요(각 세트는 1~45 사이의 6개 숫자):" %set_count)
    
    for i in range(set_count):
        while True:
            try:
                user_input = input("%d번째 세트 입력(공백으로 구분" "):" %(i+1))
                nums=[]
                for x in (user_input.split()):
                    nums.append(int(x))
                nums.sort()

                # if len(nums) != 6 or len(set(nums)) != 6 or not all(1 <= n <= 45 for n in nums):
                if len(nums) != 6:
                    raise ValueError
                elif len(set(nums)) != 6:
                    raise ValueError
                for n in nums:
                    if not (1 <= n <= 45):
                        raise ValueError
                
                user_numbers.append(nums)
                break
            except ValueError:
                print("잘못된 입력입니다. 1~45 사이의 중복되지 않은 숫자 6개를 입력하세요.")
    return user_numbers

# set_count 개수만큼 로또 번호 자동으로 생성하기
def user_lotto_numbers_auto(set_count):
    user_numbers = []
    for i in range(set_count):
        for x in 6:
            num=
            user_numbers.append()
    user_numbers.sort()
    return user_numbers

# 자동으로 번호 만들기
#####################################################

def check_results(user_numbers, winning_numbers):
    # 구매자의 로또 번호와 당첨 번호 비교
    print("당첨 번호:", winning_numbers)
    
    count = 0
    for set in user_numbers:
        count += 1
        matched = 0
        for num in set:
            for winning_number in winning_numbers:
                if num == winning_number:
                    matched += 1
                    break       # 꼭 필요한가?

        if matched == 6:
            print("%d번째 세트 %s => %d개 일치 => 1등입니다!!!" % (count, set, matched))
        elif matched == 5:
            print("%d번째 세트 %s => %d개 일치 => 2등입니다!!!" % (count, set, matched))
        elif matched == 4:
            print("%d번째 세트 %s => %d개 일치 => 3등입니다!!!" % (count, set, matched))
        else:
            print("%d번째 세트 %s => %d개 일치" % (count, set, matched))



# 실행 부분
set_count = get_purchase_amount()  # 로또 구매 세트 개수 입력받기
#수동으로할지 자동으로할지 정하기
user_numbers = user_lotto_numbers(set_count)  # 사용자 로또 번호 입력받기
check_results(user_numbers, winning_numbers)  # 결과 비교