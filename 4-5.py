s= input("단어 입력 : ")
i=len(s)-1     #len()은 1부터 시작인데 [] 이거는 인덱스라서 0부터 시작 이부분 주의 하기!
x=""
while i>=0:
    x=s[i]
    if s[i]==" ":
        x="-"
    i=i-1
    print(x,end="")