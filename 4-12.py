for i in range(9,0,-1):
    print(str(i)*(i))

for i in range(9,0,-1):
    for j in range(i):
        print(i, end=" ")
    print()