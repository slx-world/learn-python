"""
@Author: Song Laixiong
@Create: 2024-03-17
@Describe: 条件语句
"""

if True:
    print('条件成立执行的代码1')
    print('条件成立执行的代码2')

# 下方的代码没有缩进到if语句块，所以和if条件无关
print('我是无论条件是否成立都要执行的代码')

# age = 20
# if age >= 18:
#     print('已经成年，可以上网')
#
# print('系统关闭')
#
# age = int(input('请输入您的年龄：'))
#
# if age >= 18:
#     print(f'您的年龄是{age}，已经成年，可以上网')
#
# print('系统关闭')
#
# age = int(input('请输入您的年龄：'))
#
# if age >= 18:
#     print(f'您的年龄是{age}，已经成年，可以上网')
# else:
#     print(f'您的年龄是{age}，未成年，请自行回家写作业')
#
# print('系统关闭')

age = int(input('请输入您的年龄：'))
if age < 18:
    print(f'您的年龄是{age}，童工一枚')
elif age <= 60:
    print(f'您的年龄是{age}，合法工龄')
elif age > 60:
    print(f'您的年龄是{age}，可以退休')

""""
    1、如果有钱，则可以上车
        2、上车后，如果有空座，可以坐下
        上车后，如果没有空位，则站着等空座位
    如果没钱，不能上车
"""
# 假设用money = 1表示有钱，money = 0表示没钱
# seat = 1表示有空座，seat = 0表示没有空座
money = 1
seat = 0

if money == 1:
    print('土豪，不差钱，顺利上车')
    if seat ==1:
        print('有空位，可以坐下')
    else:
        print('没有空座，站等')
else:
    print('没钱，不能上车，追着公交车跑')

import random
computer = random.randint(0, 2)
print(computer)
player = int(input('请出拳：0-石头，1-剪刀，2-布'))

if (((player == 0) and (computer == 1)) or ((player == 1) and (computer == 2)) or ((player == 2) and (computer == 0))):
    print('玩家获胜')
elif player == computer:
    print('平局')
else:
    print('电脑获胜')

a = 1
b = 2
c = a if a > b else b
print(c)
