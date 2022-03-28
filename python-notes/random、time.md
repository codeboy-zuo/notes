## random模块

```python
import random

range(num)		# 生成0到(num-1)的数
range(min, max)		# 生成min到(max-1)的数
random.random()		# 生成一个随机的浮点数，范围是在0.0~1.0之间。
random.uniform(min, max)	# 可以设定 浮点数 的范围，一个是上限，一个是下限。
random.randint(min, max)	# 随机生一个 整数int 类型，可以指定这个整数的范围，同样有上限和下限值。

random.choice()		# 可以从任何序列，选取一个随机的元素返回，可以用于字符串、列表、元组等。
list = [1, 2, 3]
print(random.choice(list))

random.shuffle()	# 可以将一个序列中的元素随机打乱,打乱后再进行打印等操作(不适用于元组、字典、集合)
list = ['1', '2', '3']
random.shuffle(list)
print(list)

random.sample()		# 可以从指定的序列中，随机的截取指定长度的片断，不作原地修改。
list = ['1', '2', '3']
print(random.sample(list, 1))
```

## time模块

```python
import time

time.time()		# 传回的是1970年1月1日00:00:00AM至今的秒数

# 可利用此来计算执行一段程序所花费时间
start_time = time.time()
	# <程序……>
end_time = time.time()
print('所花费时间为：%d 秒' % (end_time - start_time))

time.sleep(2)	# 等待2s
time.asctime()	# 获取系统时间	Mon Mar 28 23:02:59 2022
time.localtime()		
# 获取当前时间time.struct_time(tm_year=2022, tm_mon=3, tm_mday=28, tm_hour=22, tm_min=59, tm_sec=10, tm_wday=0, tm_yday=87, tm_isdst=0)
```
