# 题目：字符串排序。

str1 = input("输入字符串")
str2 = input("输入字符串")
str3 = input("输入字符串")

if str1 > str2: str2, str1 = str1, str2
if str1 > str3: str3, str1 = str1, str3
if str2 > str3: str2, str3 = str3, str2
print(str1, str2, str3)
