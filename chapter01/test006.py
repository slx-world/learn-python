"""
@Author: Song Laixiong
@Create: 2024-03-17
@Describe: 运算符
"""

num = 1
print(num)

num1, float1, str1 = 10, 0.5, 'hello world'
print(num1)
print(float1)
print(str1)

a = b = 10
print(a)
print(b)

a = 100
a += 1
print(a)

b = 100
b *= 3
print(b)

c = 10
c += 1 + 2
# 输出13，先算运算符右侧1 + 2 = 3，c += 2，推导出c = 10 + 3
print(c)

a = 7
b = 5
print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)

a = 1
b = 2
c = 3
print((a < b) and (b < c))
print((a > b) and (b < c))
print((a > b) or (b < c))
print(not (a > b))

a = 0
b = 1
c = 2
# and运算符，只要有一个值为0，则结果为0，否则结果为最后一个非0数字
print(a and b)
print(b and a)
print(a and c)
print(c and a)
print(b and c)
print(c and b)
# or运算符，只有所有值为0，结果才为0，否则结果为第一个非0数字
print(a or b)
print(a or c)
print(b or c)