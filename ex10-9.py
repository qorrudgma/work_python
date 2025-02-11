# try:
#     print(x)
# except NameError:
#     print("변수가 정의되지 않아 오류가 발생함!")

# ===============================

def divide(a,b):
    try:
        c=a/b
    except ZeroDivisionError:
        print("0 나누기 오류가 발생함!")
    else:
        print(c)

divide(30,10)