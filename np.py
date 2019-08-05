import numpy as np

# .shape 获取数组的大小 几行几列
# .dtype 获取元素属性  int 等
# .size 元素总数

# 结构数组  定义数组类型persontype， 创建数组时直接指定 dtype = persontype
# np.mean() 取平均值    获取年龄  ages = peoples[:]['age']
persontype = np.dtype({
    'names': ['name', 'age', 'chinese', 'math', 'english'],
    'formats': ['S32', 'int', 'int', 'int', 'float']
})

peoples = np.array([('zhangsan', 20, 79, 88, 89), ('lisi', 19, 90, 97, 98.5),
                    ('wangwu', 18, 99, 18, 90.5), ],
                   dtype=persontype)
ages = peoples[:]['age']
chinese = peoples[:]['chinese']
math = peoples[:]['math']
english = peoples[:]['english']
print('------结构数组------')
print(np.mean(ages))
print(np.mean(chinese))
print(np.mean(math))
print(np.mean(english))

# 数学运算
# np.arange(a,b,c)  三个参数 起点为a，终点为b，步长为c
x1 = np.arange(1, 15, 2)
# np.linspace(a,b,c,endpoint = True,retstep = False,dtype = None) 三个参数 起点为a，终点为b，要生成的样本数。默认是50
# endpoint(bool型)：如果是True，'stop'是最后样本。否则不包含'stop'。
# retstep(bool型)：如果是True，返回('samples', 'step')
x2 = np.linspace(1, 13, 7)
print('------数学运算------')
print(x1.dtype)
print(x2.dtype)
print(np.add(x1, x2))  # 加
print(np.subtract(x1, x2))  # 减
print(np.multiply(x1, x2))  # 乘
print(np.divide(x1, x2))  # 除
print(np.power(x1, x2))  # 求 n 次方
print(np.remainder(x1, x2))  # 取余

# 统计函数
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print('------统计函数------')
print(a)
print(a.shape)
print(np.amin(a))
# 如果不知道axis，这相当于把多维数组展开成一维，然后求这个一维数组里所有元素的和。
print(np.amin(a, 0))  # axis=0，按第一维（行）上的元素找最大值，不用管列向量的个数（列数不变），每一列都这样做
print(np.amin(a, 1))  # axis=1，按第二维（列）上的元素找最大值，不用管行向量的个数（行数不变），每一行都这样做。
print(np.amax(a))
print(np.amax(a, 0))
print(np.amax(a, 1))















