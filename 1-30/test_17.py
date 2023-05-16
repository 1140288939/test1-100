# 一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
import math

for i in range(2, 1001):
    list1 = [1]
    n = i
    k = 2
    sum1 = 0
    sqrt1 = math.sqrt(i)
    while k <= sqrt1:
        if i % k == 0:
            list1.append(k)
            list1.append(i // k)
        k += 1
    for j in list1:
        sum1 += j
    if sum1 == i:
        print(i)
        list1.sort()
        for j in list1:
            print(j, end=" ")
        print()

