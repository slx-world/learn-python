"""
@Author: Song Laixiong
@Create: 2024-03-16
@Describe: 输出
"""

print('hello Python')

# age = 18
# print(age)
# print(f'今年我的年龄是{age}岁')
# print('今年我的年龄是%d岁' % age)

age = 18
name = 'TOM'
weight = 75.5
student_id = 1
print('我的名字是%s' % name)
print('我的学号是%4d' % student_id)
print('我的体重是%.2f公斤' % weight)
print('我的名字是%s，今年%d岁了' % (name, age))
print('我的名字是%s，明年%d岁了' % (name, age + 1))
print(f'我的名字是{name}, 明年{age + 1}岁了')

print('输出的内容', end="\n")
print('内容', end="")