# 题目：求0—7所能组成的奇数个数。
# 程序分析：
# 组成1位数是4个。
# 组成2位数是7*4个。
# 组成3位数是7*8*4个。
# 组成4位数是7*8*8*4个。
# ......
import math

sum = 4

for i in range(7):
    print(int(sum))
    sum += 7 * math.pow(8, i) * 4
print("sum=", int(sum))