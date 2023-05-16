# 题目：找到年龄最大的人，并输出。请找出程序中有什么问题。

person = {"li": 18, "wang": 50, "zhang": 20, "sun": 62}
m = 'li'
for i in person.keys():
    if person[m] < person[i]:
        m = i
print("%s,%d" % (m, person[m]))
