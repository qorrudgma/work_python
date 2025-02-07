# sum=0
# i=1
# while i<=10:
#     sum+=i
#     i+=1
# print(sum)

# sum=0
# i=500
# while i<=600:
#     if i%5==0:
#         sum+=i
#     i+=1
# print("5의 배수 합계: %d"%sum)

s="Python is widely used by a number of big companies"
i=0
count=0
print("모음 : ", end="")
while i<len(s): #i<=len(s)-1
    if (s[i].lower()=="a" or s[i].lower()=="e" or s[i].lower()=="i"
        or s[i].lower()=="o" or s[i].lower()=="u"):
        count+=1
        print(s[i], end=", ")
    i+=1
print("\n모음 개수 : %d" %count)
