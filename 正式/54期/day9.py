"""
文本文件需要字符编码
二进制形式不能指定编码格式
二进制只能写二进制   但是可以通过编码，将字符转换为二进制

"""

with open('1.txt', 'w', encoding='utf-8') as a, open(r'C:\Users\赵鑫杰\Desktop\字幕\第一个.srt', 'rb') as f:
    content = f.read().decode('utf-8')
    a.write(content)
print('over!')

"""
读取文件的详细操作
read()  读取到最后
read(数字)
    1.如果是b模式   表示读取多少个字节
    2.如果是t模式   表示读取多少个字符
    

"""





