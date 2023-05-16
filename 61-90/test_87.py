# 时间函数举例1。

import time

print(time.time())
# Convert a time in seconds
print(time.ctime(time.time()))
print(time.localtime())
#  asctime()---->Convert a time tuple to a string, e.g. 'Sat Jun 06 16:26:11 1998'.
#  localtime()--->Convert seconds since the Epoch to a time tuple expressing local time.
print(time.asctime(time.localtime(time.time())))
# gmtime([seconds]) -> (tm_year, tm_mon, tm_mday, tm_hour, tm_min,
#                       tm_sec, tm_wday, tm_yday, tm_isdst)
print(time.asctime(time.gmtime(time.time())))
print(time.asctime())
# Convert a time tuple in local time to seconds since the Epoch.
print(time.mktime(time.localtime()))
