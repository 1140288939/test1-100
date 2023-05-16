# 题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
#
# 程序分析：利用 while 或 for 语句,条件为输入的字符不为 '\n'。

str1 = input("输入一段字符串")
spaceNum, letterNum, otherNum = 0, 0, 0
for c in str1:
    if c == "\n":
        break
    if c == " ":
        spaceNum += 1
    elif c.isalpha():
        letterNum += 1
    else:
        otherNum += 1
print("spaceNum:", spaceNum, "letterNum:", letterNum, "otherNum:", otherNum)
