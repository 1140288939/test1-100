# 对10个数进行排序。
# 程序分析：可以利用选择法，即从后9个比较过程中，选择一个最小的与第一个元素交换，下次类推，即用第二个元素与后8个进行比较，并进行交换。

list1 = [7, 6, 9, 1, 22, 343, 666, 89, 8, 99]

for i in range(9):
    l = i
    flag = False
    for j in range(i+1, 10):
        if list1[l] > list1[j]:
                l = j
                flag = True
    if flag == True:
        temp = list1[i]
        list1[i] = list1[l]
        list1[l] = temp
for i in list1:
    print(i)