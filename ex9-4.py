import time

seconds=time.time()
1739245456.6732616
print(seconds)              #그리니치 천문대 기준으로 1970년 1월1일 0시 0분 0초 부터 경과된 시간(밀리세컨드)

tm=time.gmtime()
print(tm)

# tm2=time.localtime(1739245456.6732616)  #지난 시간 기준으로 지금 몇시인지 구한다
tm2=time.localtime(seconds)         #계속 변경해줌 바로바로
print(tm2.tm_year,"년")
print(tm2.tm_mon,"월")
print(tm2.tm_mday,"일")
print(tm2.tm_hour,"시")
print(tm2.tm_min,"분")
print(tm2.tm_sec,"초")