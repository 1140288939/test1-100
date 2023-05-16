# 列表使用实例

testList = [10086, '中国移动', [1, 2, 4, 5]]
print(len(testList))
print(testList[1:])
testList.append("I\'m new here")
print(testList, testList[-1])
print(len(testList))
# 不包括最后一个
print(testList[:-1])
# 删除最后一个
print(testList.pop())
print(len(testList))
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1])
newlist = [i[1] for i in matrix if i[1] % 2 == 0]
print(newlist)