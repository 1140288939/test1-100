# 题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
#  程序分析：兔子的规律为数列1,1,2,3,5,8,13,21



while True:
    count = int(input())
    for _ in range(count-1):
        i0 = 0
        i1 = 1
        list = [i1]
        for _ in range(_):
         temp = i0
         i0 = i1
         i1 = temp + i1
         list.append(i1)
        print(list)
