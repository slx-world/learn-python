"""
@Author: Song Laixiong
@Create: 2024-03-16
@Describe: 转换数据类型
"""

# num = input('请输入您的幸运数字：')
# print(f'您的幸运数字是{num}')
# print(type(num))
# print(type(int(num)))

num1 = 1
print(float(num1))
print(type(float(num1)))

num2 = 10
print(type(str(num2)))

list1 = [10, 20, 30]
print(tuple(list1))
print(type(tuple(list1)))

t1 = (100, 200, 300)
print(list(t1))
print(type(list(t1)))

# eval()将字符串中的数据转换成Python表达式原本类型
str1 = '10'
str2 = '[1, 2, 3]'
str3 = '(100, 200, 300)'
str4 = "'name': 'TOM', 'age': 14"
print(eval(str1))
print(eval(str2))
print(eval(str3))
# print(eval(str4))
print(type(eval(str1)))
print(type(eval(str2)))
print(type(eval(str3)))

