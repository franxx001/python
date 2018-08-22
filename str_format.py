age = 20
name = 'Swaroop'
print('{0} was {1} years old when he wrote this book'.format(name, age))
print('why is {0} playing with that python?'.format(name))
print('{} was {} years old when he wrote this book'.format(name, age))
print('why is {} playing with that python?'.format(name))

# 对于浮点数 '0.333' 保留小数点(.)后三位
print('{0:.3f}'.format(1.0 / 3))
# 使用下划线填充文本，并保持文字处于中间位置
# 使用 (^) 定义 '___hello___'字符串长度为 11
print('{0:_^11}'.format('hello'))
# 基于关键词输出 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))
# print 总是会以一个不可见的“新一行”字符（\n）结尾
# 防止打印过程中出现这一换行符，你可以通过 end 指定其应以空白结尾
print('a', end='')
print('b', end=' ')
print('c')
# 转义字符
print('this is the first line\nthis is the second line')
print('this is the frist sentence.\
this is the second sentence')
# 原始字符串
print(r'newlines are indicated by \n')
print('newlines are indicated by \\n')
