#다시보기

tup=(10,20,30,40,50)

def sum_tup(numbers):
    total=0
    for number in numbers:
        total+=number
    return total

total=sum_tup(tup)

print(total)