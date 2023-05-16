# 题目：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位

l = []
for i in range(0, 5):
    l.append(i+1)
print(l)
i, j = 0, 0
while len(l) > 1:
    length = len(l)
    print("length", length)
    if (i+1) % 3 == 0:
            # print(i, length)
            l[j % length] = 999
            # print(l)
            l.remove(999)
            print(l)
            j -= 1
    i += 1
    j += 1
    j %= length
    print("i,j", i,j)
print(l)