# 求100之内的素数。
import math
print(2)
print(3)
for i in range(2, 101):
    s = math.sqrt(i)
    s = int(s)
    for j in range(2, s+1):
        if i % j == 0:
            break
        if j == s:
            print(i)