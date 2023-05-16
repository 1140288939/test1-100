# 题目：输出指定格式的日期。
#
# 程序分析：使用 datetime 模块。
import datetime
# %Y %m %d %H %M %S
if __name__ == "__main__":
    print(datetime.date.today().strftime("%d/%m/%Y %H:%M:%S"))
    dt = datetime.date(2020, 8, 10)
    print(dt.strftime("%d/%m/%Y"))
    # 日期算术运算
    dt = dt + datetime.timedelta(days=30)
    print(dt.strftime("%d/%m/%Y"))
    # 替换日期
    dt = dt.replace(year=dt.year+1)
    print(dt.strftime("%d/%m/%Y"))
