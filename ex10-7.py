# import csv

# file_name = "weather.csv"
# f = open(file_name,"r",encoding="utf-8")
# lines = csv.reader(f)   #파일 전체를 읽어옴

# for line in lines:
#     print(line)

# f.close()

#==============================================

# import json
# member = {"id":"swhong",
#  "name":"홍성우",
#  "age":23,
#  "history":[
#      {"date":"2021-03-15","route":"mobile"},
#      {"date":"2020-06-23","route":"pc"}
#  ]
# }

# # dumps: member딕셔너리를 json으로 인코딩
# # ensure_ascii=False => 아스키 형태로 저장 XX
# # indent=4 => 4칸 들여쓰기
# json_string = json.dumps(member, ensure_ascii=False, indent=4)
# print(json_string)

# ============================================

# import json
# member = {"id":"swhong",
#  "name":"홍성우",
#  "age":23,
#  "history":[
#      {"date":"2021-03-15","route":"mobile"},
#      {"date":"2020-06-23","route":"pc"}
#  ]
# }
# with open("member.json","w",encoding="utf-8") as f:
#     # json.dumps(member, f, ensure_ascii=False, indent=4)
#     # dump(): 딕셔너리를 json파일로 생성
#     json.dump(member, f, ensure_ascii=False, indent=4)

# ============================================

import json
# load: json파일을 디코딩해서 딕셔너리로 저장
with open("member.json","r",encoding="utf-8") as f:
    dict = json.load(f)
    print(dict)