# 某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：每位数字都加上5,
# 然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换.

x = int(input("输入一个四位数\n"))
l = []
while x > 0:
    l.append(x % 10)
    x //= 10
for i in range(4):
    l[i] = (l[i]+5) % 10
print(l)


