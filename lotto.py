import random

# 로또 당첨 번호 생성 (1~45 중 6개 랜덤 선택)
with open("lotto.txt", "r", encoding="utf-8") as win:
    numbers = win.readline()
    winning_numbers=[]
    for win_number in numbers.split():
        winning_numbers.append(int(win_number))

# 사용자로부터 로또 구매 금액 입력받기
def get_purchase_amount():
    while True:
        try:
            amount = int(input("구매할 금액을 입력하세요 (1세트 = 1,000원): "))
            if amount < 1000 or amount % 1000 != 0:
                # raise: 에러를 강제로 발생시킨다
                raise ValueError
            return amount // 1000   # amount / 5000를 사용하면 실수형이되버려서 n.0이라 몫만 반환환
        except ValueError:
            print("잘못된 입력입니다. 1,000원 단위로 입력하세요.")

def user_lotto_numbers(set_count):
    # 사용자로부터 set_count 개수만큼 로또 번호 입력받기
    user_numbers = []
    print("총 %d세트의 로또 번호를 입력하세요 (각 세트는 1~45 사이의 6개 숫자):" %set_count)
    
    for i in range(set_count):
        while True:
            try:
                user_input = input("%d번째 세트 입력 (공백으로 구분" "): " %(i+1))
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

def check_results(user_numbers, winning_numbers):
    # 사용자의 로또 번호와 당첨 번호 비교
    print("당첨 번호:", winning_numbers)
    
    count = 0
    for set in user_numbers:
        count += 1
        matched = 0
        for num in set:
            for winning_number in winning_numbers:
                if num == winning_number:
                    matched += 1
                    break

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
user_numbers = user_lotto_numbers(set_count)  # 사용자 로또 번호 입력받기
check_results(user_numbers, winning_numbers)  # 결과 비교