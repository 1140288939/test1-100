# 题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
#
# 程序分析：关键是计算出每一项的值。

num = int(input("输入一个单数字"))
n = int(input("输入要计算的个数"))
sum = 0
temp = 0
for _ in range(n):
    sum += temp*10 + num
    temp = temp*10 + num
    print(temp)
print(sum)
