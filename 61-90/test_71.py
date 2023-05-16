# 列表排序及连接。

a = [9, 5, 6]
b = [4, 7, 1]

print(a)
a.sort()
print(a)
print(b)
b.sort()
print(b)

# 连接列表 a 与 b
print(a + b)

# 连接列表 a 与 b
a.extend(b)
a.sort()
print(a)

# 简单的题目
if __name__ == '__main__':
    for i in range(5):
        n = 0
        if i != 1: n += 1
        if i == 3: n += 1
        if i == 4: n += 1
        if i != 4: n += 1
        if n == 3: print(64 + i)
