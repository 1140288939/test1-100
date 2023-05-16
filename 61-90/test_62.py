# 输入3个数a,b,c，按大小顺序输出。　　

list = []
for i in range(4):
    list.append(int(input("请输入第" + str(i+1) + "数字")))
a = int(list[0])
b = int(list[1])
c = int(list[2])


def swap(a, b):
    return b, a


if a < b:
    a, b = swap(a, b)
if a < c:
    a, c = swap(a, c)
if b < c:
    b, c = swap(b, c)

print(a, b, c)
