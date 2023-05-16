# 题目：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。

l = [1, 2, 3, 7, 9, 8]
length = len(l)
vmax = 0
for i in range(1, length):
    if l[i] > l[vmax]:
        vmax = i
l[vmax], l[0] = l[0], l[vmax]
print(l)
vmin = 1
for i in range(2, length):
    if l[i] < l[vmin]:
        vmin = i
l[vmin], l[- 1] = l[- 1], l[vmin]

print(l)
