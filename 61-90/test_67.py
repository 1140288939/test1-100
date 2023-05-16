# 编写input()和output()函数输入，输出5个学生的数据记录

stu = []
for i in range(1):
    x = []
    x.append(input("请输入第"+str(i+1)+"同学的学号"))
    x.append(input("请输入第"+str(i+1)+"同学的姓名"))
    xx = []
    for j in range(3):
        xx.append(input("请输入第"+str(j)+"个科目成绩"))
    x.append(xx)
    print("第"+str(i+1)+"个同学的信息", x)
    print("------------------------------------------------------")
    stu.append(x)
print(stu)