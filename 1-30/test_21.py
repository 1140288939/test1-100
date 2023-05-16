# 打印出如下图案（菱形）

n = int(input("输入一个奇数"))
for i in range(1, n+1):
    for j in range(n-i):
        print(end=" ")
    for k in range(i*2-1):
        print("*", end="")
    print()
for i in range(1, n):
    for j in range(i):
        print(end=" ")
    for k in range((n-i)*2-1):
        print("*", end="")
    print( )