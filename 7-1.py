km=int(input("킬로미터를 입력하세요 : "))
# def kmm():
#     m=km*0.621371
#     print("%d 킬로미터는 %0.2f 마일이다."%(km,m))
# kmm()

#==========같은 문제===========

def kmm(x):
    result=x*0.621371
    return result

mile=kmm(km)
print("%d 킬로미터는 %0.2f 마일이다."%(km,mile))