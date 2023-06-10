import re

st = '123Qwe!_@#你我他\t \n\r'
res1 = re.findall('\w', st)  # 匹配字母数字下划线
res2 = re.findall('\W', st)  # 匹配除字母数字下划线以外的
res3 = re.findall('\s', st)  # 匹配空白 制表符，换页符，转义符
res4 = re.findall('\S', st)  # 匹配除空白 制表符，换页符，转义符以外的
print(res1)
print(res2)
print(res3)
print(res4)




