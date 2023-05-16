# 题目：按逗号分隔列表。
list1 = []
for i in range(1,6):
    list1.append(str(i))
# for i in list1:
#     print(i, end="")
#     if i == list1[len(list1)-1]:
#         pass
#     else:
#         print(end=",")
print(type(list1[0]))
print(",".join(i for i in list1))
