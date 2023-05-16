# 八进制转换为十进制
import math

b = int(input("请输入一个八进制的数"))
result = 0
i = 0
# 转换
while b > 0:
    result += b % 10 * math.pow(8, i)
    b //= 10
    i += 1
print("八进制转十进制", int(result))



