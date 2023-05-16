# 结构体变量传递


class student:
    age = 0
    name = "Bob"


def f(s):
    s.age = 20
    s.name += " nn"


x = 1
s = student()
try:
    f(x)
except:
    print("Error")

f(s)
print(s.name, s.age)
