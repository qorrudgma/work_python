# import calc
# import calc as c    #calc를 c로 칭하겠다 별칭을 줌
# from calc import add    #calc에 add만 사용하겠다
from calc import add,sub    #calc에 add와 sub만 사용하겠다

# x=c.add(10,20)
x=add(10,20)
print(x)

# y=c.sub(10,20)
y=sub(10,20)
print(y)