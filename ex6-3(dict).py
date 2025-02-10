# score=dict([("국어",80),("영어",70),("수학",100)])      #딕셔너리안에 리스트 안에 튜플
# score={"국어":80,"영어":70,"수학":100}      #위랑같음
# print(score)
# print(score["수학"])        #키를 사용해서 밸류값을 가져온다

# score["음악"]=70        #음악이라는 키가 없어서 추가
# print(score)

# score["영어"]=50        #영어라는 키가 존재하기때문에 수정
# print(score)

#========================

# car={"brand":"현대","model":"아반떼","start":1990,"year":2021}
# print(car)

# x=car.pop("start")      #키에 해당하는 값을 잘라냄
# print(x)        #출력은 값만 출력 잘라내는건 통으로 잘라냄
# print(car)

# car.clear()
# print(car)      #모두삭제

#========================

area_code={"서울":"02","부산":"051","대구":"053","광주":"062"}
print(area_code)

for key in area_code:
    print("%s 지역번호: %s"%(key,area_code[key]))
