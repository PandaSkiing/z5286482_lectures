'''


x = str('abc')
xup = str.upper(x)
print(xup)

xlow = str.lower(x)
print(xlow)

y = str('1')
YUP = str.upper(y)
print(YUP)


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        # 定义如何将日期对象转换为字符串表示形式
        return f"{self.year}/{self.month:02d}/{self.day:02d}"

# 创建一个日期对象
my_date = Date(2023, 9, 15)

# 使用 str() 函数或对象的 .str 方法将日期对象转换为字符串
date_str = str(my_date)

# 打印字符串表示形式
print(date_str)  # 输出：2023-09-15


Length = int(56)
Width = int(33)
Height = float(30.5)
volume = (Length * Width * Height)
print(f"the volume of the box is {volume} cubic centimeters.")


import re
email = "From firstname.surname@unsw.edu.au Tue Oct06 10:10:15 2020"
domain = re.search(r'@([\w.-]+)', email).group(1)
print(domain)


x = ("Hello, world")
y = x.split()
print(x)
print(y)

{ }


_hello_world = "Hello James"
print(_hello_world)

x = "1788-01-26"
print(x)
x = True
print(type(x))
x = 1
print(type(x))
x = 1.0
print(type(x))
'''

w = "What"
i = "IS"
c = "CamelCase?"

formatted_string = '{} {} {}'.format(w, i.lower(), c)
print(formatted_string)

class MyClass:
    pass

# 创建一个类的实例
obj = MyClass()

# 设置属性 x 和 y 的初始值
obj.x = 0
obj.y = 0

# 执行语句
obj.x = 1
obj.y = 2
obj.y = obj.x
obj.x = obj.y

# 打印最终的属性值
print(f"obj.x = {obj.x}")
print(f"obj.y = {obj.y}")
print(obj.x)


a = "this"
b = "problem"
a = f"{a} Parsons {b}"
b = print
b(a)

t =('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
print(t[:5])

b, s, i = True, 'string', 1
print(b, s, i)

dic0 = {'a': 1, 'b': 2, 'c': 3}
print(dic0)
dic1 = dic0.update({'a': 0, 'd': 4})
print(dic1)
print(dic0)
print(dic0['a'])

tup = (1, 2, ('a', 'b'))
dic = {tup: 'value'}
print(tup)
print(dic)