list=[]
def num1(x):
    for i in range(x):
        j=i+1
        list.append(j*j)
    return list

#i*i = i**2 같음

# i=1
# def num1(x):
#     global i
#     while i<=x:
#         list.append(i*i)
#         i+=1
#     return list


# def num1(x):
#     global i
#     while i<=x:
#         list.append(i*i)
#         i+=1
#     return list


num=int(input("n값을 입력하세요 : "))
print(num1(num))