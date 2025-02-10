def string_replace(string):
    result=string.replace(" ","_")
    return result

#다른방법

# def string_replace(string):
#     result=""
#     i=0

#     while i<len(string):
#         if string[i] ==" ":
#             result+="_"
#         else:
#             result+=string[i]
#         i+=1
#     return result


str=input("문자열을 입력하세요 : ")
print(string_replace(str))