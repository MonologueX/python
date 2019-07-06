# 变量定义和常用操作

# print(100/8)
# a = 100
# b = 8
# print(a/b)

# 十二生肖
#chineseZodiac = '鼠牛虎兔龙蛇马羊猴鸡狗猪'
#print(chineseZodiac[0:4])
#print(chineseZodiac[-1])
#year = 2019
#print(chineseZodiac[year % 12 - 4])
#
#print('狗' in chineseZodiac)
#print('狗' not in chineseZodiac)
#
#print(chineseZodiac + chineseZodiac)
#print(chineseZodiac + "abcd")
#print(chineseZodiac * 3)
#zodiacName = (u'白羊座', u'金牛座', u'双子座', u'巨蟹座', u'狮子座', u'处女座', u'天秤座',
#              u'天蝎座', u'射手座', u'摩羯座', u'水瓶座', u'双鱼座')
#
#zodiacDays = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 23), (6, 22),
#              (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))
#
#(month, day) = (2, 15)
#
#zodiacDay = filter(lambda x: x<=(month, day), zodiacDays)
#print(zodiacDay)
##zodacLen = len(list((zodiacDay))%12
#
aList = ['abc', 'xyz']
aList.append('x')
print (aList)
aList.remove('xyz')
print (aList)
