# s="I am a genius!"

# list1=[]

#1번
# for x in s:
#     list1.append(x)
# print(list1)

#2번
# i=0
# while i<len(s):
#     list1.append(s[i])
#     i+=1
# print(list1)

# number=[7,9,15,18,30,-3,7,12,-16,-12]

# sum=0

#3번
# for i in number:
#     sum+=i
# print("합계:", sum)

# 4번
# i=0
# while i<len(number):
#     sum+=int(number[i])
#     i+=1
# print("합계:", sum)

#5번
# i=0
# s=0
# while i<len(number):
#     if (+1)%2==0:
#         s=int(number[i])
#         print(s)
#         sum+=s
# print(sum)

# 6번
file_names=["file1.py","file2.txt","file3.pptx","file4.doc"]

for file_name in file_names:
    arr=file_name.split(".")
    print("%s => 파일명:%s, 확장자:%s"%(file_name,arr[0],arr[1]))