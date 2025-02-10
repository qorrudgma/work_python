temp={"월":15.5,"화":17.0,"수":16.2,"목":12.9,"금":11.0,"토":10.5,"일":13.3,}
# print("-"*42)
# for m in temp:
#     print("  %s  "%m,end="")
# print()
# print("-"*42)
# for c in temp:
#     c=temp[c]
#     print(" %s "%c,end="")
# print()
# print("-"*42)

#=============================

#이거 다시해보기 6-3
# l=100
# d=""
# for t in temp:
#     if temp[t]<l:
#         l=temp[t]
#         d=t
# print(t,l)

# smallet=temp["월"]

# for key in temp:
#     print(temp[key],end=" ")
#     if temp[key]<smallet:
#         day=key
#         smallet=temp[key]
# print(day,smallet)

sum=0

for key in temp:
    sum+=float(temp[key])    #숫자로 저장해서 굳이 숫자형으로 안바꿔도된다 => sum+=temp[key]  이렇게 써도됌됌
print("일주일간 기온 평균: %.1f"%(sum/len(temp)))

print(temp["월"])           #값 그대로 나옴
print(int(temp["월"]))      #소수점이 없이 나옴(정수)
print(float(temp["월"]))    #소수점이 있이 나옴(실수)