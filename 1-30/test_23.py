# 题目：求1+2!+3!+...+20!的和。
#
# 程序分析：此程序只是把累加变成了累乘。

lc = 1
sum = 0
for i in range(1, 21):
    lc *= i
    sum += lc
print(sum)
