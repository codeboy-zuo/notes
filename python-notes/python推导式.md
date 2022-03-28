## 列表推导式

```python
"""
格式：
1 [表达式 for 变量 in 列表	# 表达式：列表生成元素表达式]
2 [表达式 for 变量 in 列表 if 条件]
"""
list = ['google', 'baidu', 'apple']
new_list = [i for i in list if len(i) > 5]
print(new_list)		# 打印['google']
```

## 元组推导式

```python
"""
格式：
1 (表达式 for 变量 in tuples)
2 (expression for item in tuples if condition)
"""
tup = (x for x in range(1, 5))
print(tup)		# <generator object <genexpr> at 0x000001C868CDD970>返回的是生成器对象
print(tuple(tup))	 # tuple()方法可转换成元组
```



## 字典推导式

```python
"""
格式：
1 {key: value for value in dic1}
2 {key: value for value in dic1 if condition}
"""
list = ['apple', 'banana', 'pear']
dic = {key: len(list) for key in list}
print(dic)		# 打印{'apple': 3, 'banana': 3, 'pear': 3}
```

## 集合推导式

```python
"""
格式：
1 {表达式 for 变量 in set}
2 {表达式 for 变量 in set if 条件}
"""
set = {'google', 'baidu', '360'}
set_1 = {i for i in set if len(i) > 3}
print(set_1)	# {'baidu', 'google'}
```

