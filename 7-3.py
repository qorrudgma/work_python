str=input("영어 문장을 입력하세요 : ")
a=input("알파벳 하나를 입력하세요 : ")

# def count(x):
#     result=str.count(x)
#     return result

# p=count(a)
# print("%s에 포함된 %s의 개수는 %d개이다."%(str,a,p))

#다른방법

def count(strng, x):
    count=0

    for i in str:
        if i==x:
            count+=1
    return count

c=count(str,a)
print("%s에 포함된 %s의 개수는 %d개이다."%(str,a,c))

#변수로 하고 적나 바로 적나 차이가있다.

# c=count(str,a)
# print("%s에 포함된 %s의 개수는 %d개이다."%(str,a,count(str,a)))
