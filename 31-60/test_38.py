# 题目：将一个数组逆序输出。
# 程序分析：用第一个与最后一个交换。

a = [5, 4, 3, 2, 1]
print(a)
for i in reversed(a):
    print(i, end=" ")
print()
for i in range(len(a) // 2):
    temp = a[i]
    a[i] = a[len(a) - 1 - i]
    a[len(a) - 1 - i] = temp
for i in a:
    print(i, end=" ")
print(a)