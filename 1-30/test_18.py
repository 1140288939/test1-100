# 题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

h = 100.0
sum = 0
for i in range(10):
    sum += h
    h /= 2
    sum += h
print("第十次落地共：", sum-h, "第十次反弹：", h)

h = 100.0
sum = 100
for i in range(9):
    h /= 2
    sum += 2*h
print("第十次落地共：", sum, "第十次反弹：", h/2)
