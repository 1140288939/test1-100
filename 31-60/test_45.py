# 题目：使用lambda来创建匿名函数。

MAXIMUM = lambda x, y: (x >= y) * x + (x < y) * y
MINIMUM = lambda x, y: (x >= y) * y + (x < y) * x

a = 10
b = 10

print("max", MAXIMUM(a, b))
print("min", MINIMUM(a, b))
