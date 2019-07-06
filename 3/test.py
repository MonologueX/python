# 文件操作
# open() read() readline() seek() write() close()
# 记录小说主要人物
#file1 = open('name.txt', 'w')
#file1.write('诸葛亮')
#file1.close()
#
#file2 = open('name.txt', 'r')
#print(file2.read())
#file2.close()
#
#file3 = open('name.txt', 'a')
#file1.write('刘备')
#file1.close()

#file4 = open('name.txt')
#print(file4.readline())
#file4.close()
#
#file5 = open('name.txt')
#for line in file5.readlines() :
#    print('#########################')
#    print(line)
#file5.close()

#file6 = open('name.txt')
#print(file6.tell())
#file6.read(1)
#print(file6.tell())
#file6.close()

file7 = open('name.txt')
print('当前文件指针的位置: %s' %file7.tell())
print('当前读取到了一个字符，字符的内容是: %s' %file7.read(1))
# 第一个参数是偏移位置，第二个位置 0:文件开头;1:当前位置;2:文件结尾
file7.seek(5, 0)
print('进行了 seek 操作!')
print('当前文件指针的位置: %s' %file7.tell())
print('当前读取到了一个字符，字符的内容是: %s' %file7.read(1))
file7.close()








