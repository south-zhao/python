"""
用python的代码 实现一下的需求
1. 以覆盖写的方式  创建一份文件  文件里面写的数据是 '我的名字是XX'
2. 读取1当中的文件的内容
3. 将2中读取到的内容以追加写的方式   写入到另外一份文件
''"""
# a = open('1.txt','w',encoding='utf-8')
# f = open('2.txt','r',encoding='utf-8')
# f.write('我的名字是老杨')
# a.close()
# 覆盖写   模式  w
# 只能写字符串
# 需要记得关闭文件
# f = open('1.txt','w',encoding='utf-8')
# f.write()
# f.close()
# print(data)
# f = open('2.txt','a',encoding='utf-8')
# f.write(data)
# f.close()
# 操作文件的三大步骤
# 硬盘的区域 = 打开文件(文件位置,操作的模式)
# 硬盘的区域.读
# 硬盘的区域.写
# 硬盘的区域.关闭
# w/a  的模式 就只能是写数据
# r    的模式 就只能是读数据
# f = open('2.txt','a',encoding='utf-8')
# f.write('哈哈')
# f.close()  # 忘记了关闭文件
# 推荐下面的写法
# with open('2.txt','a',encoding='utf-8') as f:
#     # 操作文件
#     f.write('哈哈')
# 离开了缩进后，Python会自动帮你去执行close的操作
# with open(文件路径,模式)  as 变量名:
# 对文件的操作或者任意代码
# 同时操作多份文件
# a  = open('2.txt','a',encoding='utf-8')
# a.write('哈哈')
# a.close()
# b = open('2.txt','r',encoding='utf-8')
# b.read()
# b.close()
# with open('2.txt','r',encoding='utf-8') as a,\
#         open('3.txt','w',encoding='utf-8') as b:
#     # 任意的代码或者对文件的操作
#     print(a.read())
# 变量名不要写一样的  会发生覆盖的现像了
# with open('1.txt','r+',encoding='utf-8') as f:
#     # f.write('哈哈哈11111')
#     # print(f.read())
#     f.write('哈哈哈')
# with open('1.txt','w+',encoding='utf-8') as f:
#     # f.write('哈哈哈11111')
#     print(f.read())
# f.write('哈哈哈')
# 自动帮助我去创建一份1.TXT的文件
# 在文件里面写入  哈哈哈  三个字
# 再次运行会发生什么？ 覆盖了  所谓的覆盖值得是什么？
# 将光标移动到文件的最前面    先删除一起的内容
# 追加写   光标到了文件的最后面
# 讲内容写进去没有    有问题吗？
# r  光标在哪里？     光标在最前面  往后读取光标后面的字符
# 了解知识点  不推荐使用
# w+ 只能覆盖写  a+  只能追加写  r+   只能读取
# 但是我们不推荐使用
# 虽然可以有w+,r+,a+ 让我们既可以读又可以写，但是我们不要这么去做
# 在实际中，我们应该就使用w  r   a
# 文件都是二进制的文件 但是有一种特殊的叫做文本文件
# 文本文件就有字符，所以需要字符编码
# 我要创建一份文件，这份文件里面有文字
# 1. 两种方式
# with open('1.txt','w',encoding='utf-8') as f:
#     f.write('我是文字')
# with open('1.txt','wt',encoding='utf-8') as f:
#     f.write('我是文字')
# 我要创建一份文件，这份文件里面的字符都是用utf-8的字符编码
# 我要创建一份二进制形式的文件
# 1、 二进制形式不能指定编码格式
# 2. 二进制就只能写二进制
# with open('1.txt','wb') as f:
#     f.write('我是文字'.encode())

# 二级制形式可以搞定所有的文件，但是只能写入二进制
# 如果你是字符串，就需要编码变成二进制才能写入
# 所以为了方便，如果你是文本文件，我们更推荐用t 文本模式
# 案例  使用Python的文件操作实现对任意一份文件的复制
# 复制  将以前的文件的所有的内容  全部写入一份新的的文件
# a = input('请输入您要复制的文件').strip()
# b = f'复制{a}'
# if len(a.split('.'))==1:
#     print('请输入您的后缀名')
# if a.endswith('mp4'):
#     print('不能复制')
# else:
#     with open(a,'rb') as f1,\
#         open(b,'wb') as f2:
#         f2.write(f1.read())

# for x in range(10):
#     with open(f'{x}.txt','w',encoding='utf-8') as f:
#         f.write('我是一份文件')
'''
读取文件的详细操作
read()     读到到文件的最后的内容
read(数字)
    1. 如果是b模式  表示读取多少个字节  
    2. 如果是t模式  表示读取多少个字符  主要用于这个情况  
readline()        读取一行的内容      
readline(数字)     读取一行的内容  只读取多少个字符       
readlines()       读取文件所有的内容
                 形成一个列表，将每一行的内容当做一个元素，会携带
for  变量 in  文件对象:
    变量.strip('\n')
读取文件的每一行内容  没有换行符  


'''
# with open('666.txt','rb') as f:
#     print(f.read(3)) # 3个字节   123   字符编码
#   阿拉伯数字  英文字母  符号 不管是什么编码都是一个字节
# with open('666.txt','r',encoding='utf-8') as f:
# print(f.read())
# print(f.readline())  # 只读取一行的内容
# print('*'*30)
# print(f.readline())  # 只读取一行的内容
# print('*' * 30)
# print(f.readline())
# print(f.readlines()[1])
# for x in f.readlines():
# for x in f:
#     print(x.strip('\n'))  # 去除每一行的换行符得到每一行的内容了
#     print('*'*30)
# 如果循环这个文件对象，就可以得到每一行的内容
# 循环文件，就是循环文件的每一行的内容
# 只想读取第二
# 写操作的  了解点
# with open('777.txt','w',encoding='utf-8') as f:
#     # f.write('我是第一行\n')
#     # f.write('我是第二行')
#     # f.write('我是第三行\n')
#     data = ['我是第一行\n','我是第二行\n','我是第三行\n']
#     f.writelines(data)
# 追加的效果？
# 扩展一个
# with open('1.txt','r',encoding='utf-8') as f:
#     f.seek(9)  # 控制您的光标移动多少个字节
#     print(f.tell()) # 获取光标的位置  数字也是字节
#     # utf-8 一个中文是3个字节
#     print(f.read())
# 文件的修改
'''
文件的修改可以直接改吗？ 文件的修改本质是怎样玩的？
文件对应的是硬盘空间     硬盘不可以直接修改
我们的文件修改是如何是实现的呢？ 内存中才能修改数据 
两种方式：
1中方式:
将文件内容一次性全部读入内存中，  
然后在内存中修改
再讲修改以后的数据覆盖写入原来的文件
优点:文件修改过程中，数据只有一份
缺点:占用内存

2中方式
以读的方式去打开原文件，以写的方式打开另外一份文件(临时的文件)
一行行的读取原文件内容，修改完后写入临时文件，删除原来的文件
再讲临时文件的名字改成原来的文件的名字
优点：不会占用过多的内存
缺点：文件修改过程中一份数据占了两份




'''
# 为什么这一种方式可以
# 因为在w清楚文件内容之前，就已经将文件中的数据读取到了内存了
# 用一个变量接受好了
# with open('1.txt','r',encoding='utf-8') as f1:
#     data = f1.read()
# with open('1.txt','w',encoding='utf-8') as f2:
#     f2.write(data.replace('老杨', '木易'))
# # 这种方式不行： 因为有w的存在，文件中的内容已经被清空了，所以读取不到任何数据
# with open('1.txt','r',encoding='utf-8') as f1, \
#         open('1.txt', 'a', encoding='utf-8') as f2:
#     data = f1.read()
#     print(data)
#     f2.write(data.replace('老杨', '木易'))

'''
总结
    对于文件操作 
推荐使用 with 语法  避免忘记关闭文件
with  open() as 变量名:
    pass
with  open() as 变量名1,open() as 变量名2:
    pass
文件的类型有两种
b   二进制的形式  只能是二进制 不能指定字符编码
t   默认的，文本文件  需要字符编码

文件对象 = open(文件路径,模式,字符编码) 
w   覆盖写文件     
    没有文件会创建文件，不能创建文件夹
    有文件存在，就会先清空文件的内容
a   追加写文件
    没有文件会创建文件，不能创建文件夹
    有文件存在，就会在以前的内容后面写数据
r   read  读取文件
    没有文件会报错

文件对象.read()  读取文件中的所有内容
文件对象.read(数字)   
    1. 如果是b模式  表示读取多少个字节
    2. 如果是t模式  表示读取多少个字符

文件可以循环，表示读取文件的每一行的内容
文件不能直接修改，只能在内存中修改，然后保存进文件

如果是注册的本质：追加写数据保存成文件
如果是登录： 循环的遍历文件，得到文件中的每一行的数据 
    和输入的账户密码进行对比
注册和登录的小功能 

退散  晚安    886  
'''
with open('1.txt', 'a', encoding='utf-8') as f:
    f.seek(12)
    print(f.tell())
    f.write('哈哈')




