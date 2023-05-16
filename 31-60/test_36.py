# 题目：求一个3*3矩阵主对角线元素之和。
#
# 程序分析：利用双重for循环控制输入二维数组，再将a[i][i]累加后输出。
# list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# sum = 0
# for i in range(3):
#     for j in range(3):
#         if i == j:
#             print(list1[i][i])
#             sum += list1[i][i]
# print(sum)

list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sum1 = 0
for i in range(3):
    sum1 += list1[i][i]
print(sum1)
