# 题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
#
# 程序分析：首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。

a = [1, 2, 3, 4, 5, 6, 7]
x = input("输入一个数")
x= int(x)
if x > a[len(a)-1]:
    a.append(x)
else:
    for i in range(len(a)):
        if x > a[i]:
          continue
        else:
           a.insert(i, x)
           break
for i in a:
    print(i)
