import random

# 당첨 번호 파일 읽기
with open("lotto.txt", "r", encoding="utf-8") as win:
    numbers = win.readline()
    winning_numbers=[]
    for win_number in numbers.split():
        winning_numbers.append(int(win_number))
    winning_numbers.sort()

# 구매자로부터 로또 구매 금액 입력받기
def get_purchase_amount():
    while True:
        try:
            amount = int(input("구매할 금액을 입력하세요 (1세트 = 1,000원)D: "))
            if amount < 1000 or amount % 1000 != 0:
                raise ValueError
            return amount // 1000  # 구매 가능한 세트 개수 반환
        except ValueError:
            print("잘못된 입력입니다. 1,000원 단위로 입력하세요.")

# 수동/자동 선택
def lotto_type(set_count):
    while True:
        lotto_mode = input("'수동/자동'을 선택하여 입력하세요: ")
        if lotto_mode == "수동":
            return user_lotto_numbers(set_count)  # 수동 입력
        elif lotto_mode == "자동":
            return user_lotto_numbers_auto(set_count)  # 자동 생성
        else:
            print("잘못된 입력입니다. '수동'또는 '자동'을 입력하세요.")

# 수동 번호 입력
def user_lotto_numbers(set_count):
    user_numbers = []
    print("총 %d세트의 로또 번호를 입력하세요 (각 세트는 1~45 사이의 6개 숫자):" %set_count)
    
    for i in range(set_count):
        while True:
            try:
                user_input = input("%d번째 세트 입력 (공백으로 구분): " %(i+1))
                nums=[]
                for num_str in user_input.split():
                    num=int(num_str)
                    if not (1 <= num <= 45):
                        raise ValueError("1~45 사이의 숫자만 입력하세요.")
                    nums.append(num)
                nums.sort()
                # 중복, 개수, 범위 체크
                if len(set(nums)) != 6:
                    raise ValueError
                user_numbers.append(nums)
                break
            except ValueError:
                print("잘못된 입력입니다. 중복되지 않은 숫자 6개를 입력하세요.")
    return user_numbers

# 자동 번호 생성
def user_lotto_numbers_auto(set_count):
    user_numbers = []
    for i in range(set_count):
        nums = set()
        while len(nums) < 6:
            num = random.randint(1, 45)
            nums.add(num)
        nums = list(nums)
        nums.sort()
        user_numbers.append(nums)
        print("%d번째 세트: %s" %(i+1, nums)) 
    return user_numbers

# 당첨 결과 확인
def check_results(user_numbers, winning_numbers):
    print("\n당첨 번호: %s\n" %winning_numbers)

    # for count, user_set in enumerate(user_numbers, start=1):
    #     matched = sum(1 for num in user_set if num in winning_numbers)  # 일치 개수 계산
    count = 0
    for user_set in user_numbers:
        count += 1
        matched = 0
        for num in user_set:
            for winning_number in winning_numbers:
                if num == winning_number:
                    matched += 1
        if matched == 6:
            print("%d번째 세트 %s => %d개 일치 => 1등 당첨!!!" %(count, user_set, matched))
        elif matched == 5:
            print("%d번째 세트 %s => %d개 일치 => 2등 당첨!" %(count, user_set, matched))
        elif matched == 4:
            print("%d번째 세트 %s => %d개 일치 => 3등!" %(count, user_set, matched))
        else:
            print("%d번째 세트 %s => %d개 일치" %(count, user_set, matched))

set_count = get_purchase_amount()  # 로또 구매 세트 개수 입력받기
user_numbers = lotto_type(set_count)  # 수동 또는 자동 선택하여 번호 생성
check_results(user_numbers, winning_numbers)  # 결과 확인