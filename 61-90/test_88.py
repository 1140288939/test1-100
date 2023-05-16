# 时间案例

import time

start = time.time()
for i in range(3000):
    print(i)
end = time.time()
print(end-start)

start = time.clock()
print(start)
for i in range(10000):
    print(i)
end = time.clock()
print('different is %6.3f' % (end - start))