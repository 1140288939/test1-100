# 字符串日期转换为易读的日期格式。

from dateutil import parser
import datetime
# date time

d = datetime.datetime.now()
#"  18:00:01 2021 1 Oct"
# 21是年份 且当成了日
# 21 Nov 17 05:45:37
# 2017-11-21 05:45:37
d = d.strftime("%d %B %y %I:%M:%S")
print(d)
dt = parser.parse(d)

print(dt)
# 最后一个数字当年
t = parser.parse("21 Nov 117  12:00AM")
print(t)
