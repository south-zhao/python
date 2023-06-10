# TODO 输出有颜色的字
# print("\033[36;40m生鲜鱼白\033[0m")
"""
格式：print("\033[前景色;背景色m内容\033[0m") print("\033[31;40m两次输入的密码不一致\033[0m")

颜色      前景色      背景色

黑色      30          40
红色      31          41
绿色      32          42
黄色      33          43
蓝色      34          44
紫红色     35          45
青蓝色     36          46
白色      37          47
"""

# TODO Day 11
"""
1.
    利用函数,实现对任意一份文件的复制
2.
    利用函数和参数，实现对两个数字比较大小，
    返回更大的数字
3.
    利用文件操作实现，将用户输入的账户和密码，
    以追加的方式保存成文件db.txt
4.
    利用文件操作，实现将用户输入的账户和密码，
    与db.txt文件里面的账户和密码进行对比，
    如果账户和密码都对，则提示登录成功，
    如果都对比不上，则提示账户或密码错误
"""


# # 1.
# # 创建一个需要复制的文件
# with open("test1.txt", "w", encoding="utf-8") as f:
#     f.write("生鲜鱼白")
#
# # 复制文件的函数
# def copy(file):
#     with open(file, "rb") as f1, \
#             open(f"copy-{file}", "wb") as f2:
#         f2.write(f1.read())
#         print("文件复制成功")
#
# # 调用函数
# copy("test1.txt")

# # 2.
# # 比较a和b
# def compare(a, b):
#     if a > b:
#         return str(a) + "更大"
#     elif b > a:
#         return str(b) + "更大"
#
# # 调用函数
# print(compare(520, 1314))

# 3. 4.
# 注册账号密码
def register():
    while True:
        account = input("账号：")
        admin = input("密码：")
        admin1 = input("请再次输入密码：")
        if admin != admin1:
            print("\033[31;40m两次输入的密码不一致\033[0m")
            continue
        else:
            with open("db.txt", "r", encoding="utf-8") as f1:
                dic = eval(f1.read())
            if account in dic:
                print("\033[31;40m已存在该账号\033[0m")
                continue
            else:
                dic[account] = admin
                with open("db.txt", "w", encoding="utf-8") as f1:
                    f1.write(str(dic))
                print("\033[32;40m账号注册成功\033[0m")
                while True:
                    print("您可以选择：\n\033[36m【登录账号】\033[0m\033[31m【退出系统】\033[0m")
                    choose1 = input("您的选择是：")
                    if choose1 == "登录账号":
                        login()
                        break
                    elif choose1 == "退出系统":
                        break
                    else:
                        print("\033[31;40m并没有该选项\033[0m")
            break


# 登录账号
def login():
    with open("db.txt", "r", encoding="utf-8") as f:
        dic = eval(f.read())
    while True:
        account = input("请输入您的账号：")
        password = input("请输入您的密码：")
        if account in dic and password == dic[account]:
            print("\033[32;40m登录成功\033[0m")
            break
        elif account not in dic:
            print("\033[31;40m不存在此账号\033[0m")
        elif account in dic and password != dic[account]:
            while True:
                print("\033[31;40m您的密码输入错误\033[0m")
                password = input("请再次输入您的密码：")
                if password == dic[account]:
                    print("\033[32;40m登录成功\033[0m")
                    break
            break


# 修改密码
def revise():
    with open("db.txt", "r", encoding="utf-8") as f:
        dic = eval(f.read())
    while True:
        account = input("请输入您的账号：")
        password = input("请输入您的密码：")
        if account in dic and password == dic[account]:
            new_password = input("请输入您的新密码：")
            dic[account] = new_password
            with open("db.txt", "w", encoding="utf-8") as f1:
                f1.write(str(dic))
            print("\033[32;40m修改成功\033[0m")
            while True:
                print("您可以选择：\n\033[36m【登录账号】\033[0m\033[31m【退出系统】\033[0m")
                choose1 = input("您的选择是：")
                if choose1 == "登录账号":
                    login()
                    break
                elif choose1 == "退出系统":
                    break
                else:
                    print("\033[31;40m并没有该选项\033[0m")
            break
        elif account not in dic:
            print("\033[31;40m不存在此账号\033[0m")
        elif account in dic and password != dic[account]:
            while True:
                print("\033[31;40m您的密码输入错误\033[0m")
                password = input("请再次输入您的密码：")
                if password == dic[account]:
                    new_password = input("请输入您的新密码：")
                    dic[account] = new_password
                    with open("db.txt", "w", encoding="utf-8") as f1:
                        f1.write(str(dic))
                    print("\033[32;40m修改成功\033[0m")
                    while True:
                        print("您可以选择：\n\033[36m【登录账号】\033[0m\033[31m【退出系统】\033[0m")
                        choose1 = input("您的选择是：")
                        if choose1 == "登录账号":
                            login()
                            break
                        elif choose1 == "退出系统":
                            break
                        else:
                            print("\033[31;40m并没有该选项\033[0m")
                    break
            break


# 注销账号
def cancel():
    with open("db.txt", "r", encoding="utf-8") as f:
        dic = eval(f.read())
    while True:
        account = input("请输入您的账号：")
        password = input("请输入您的密码：")
        if account in dic and password == dic[account]:
            del dic[account]
            with open("db.txt", "w", encoding="utf-8") as f1:
                f1.write(str(dic))
            print("\033[32;40m注销成功\033[0m")
            while True:
                print("您可以选择：\n\033[36m【注册账号】\033[0m\033[31m【退出系统】\033[0m")
                choose1 = input("您的选择是：")
                if choose1 == "注册账号":
                    register()
                    break
                elif choose1 == "退出系统":
                    break
                else:
                    print("\033[31;40m并没有该选项\033[0m")
            break
        elif account not in dic:
            print("\033[31;40m不存在此账号\033[0m")
        elif account in dic and password != dic[account]:
            while True:
                print("\033[31;40m您的密码输入错误\033[0m")
                password = input("请再次输入您的密码：")
                if password == dic[account]:
                    del dic[account]
                    with open("db.txt", "w", encoding="utf-8") as f1:
                        f1.write(str(dic))
                    print("\033[32;40m注销成功\033[0m")
                    while True:
                        print("您可以选择：\n\033[36m【注册账号】\033[0m\033[31m【退出系统】\033[0m")
                        choose1 = input("您的选择是：")
                        if choose1 == "注册账号":
                            register()
                            break
                        elif choose1 == "退出系统":
                            break
                        else:
                            print("\033[31;40m并没有该选项\033[0m")
                    break
            break

print("\033[33;40m欢迎使用星茫系统\033[0m\n\
    您可以选择\n\
    \033[36m【登录账号】【注册账号】\033[0m\n\
    \033[36m【修改密码】【注销账号】\033[0m\n\
    \033[31m【退出系统】\033[0m")
with open("db.txt", "a", encoding="utf-8") as f:
    f.write("")
with open("db.txt", "r", encoding="utf-8") as f:
    judge = f.read()
if judge == "":
    with open("db.txt", "w", encoding="utf-8") as f:
        f.write('{"":""}')
while True:
    choose = input("请输入您的选择:")
    if choose == "登录账号":
        login()
        break
    elif choose == "注册账号":
        register()
        break
    elif choose == "修改密码":
        revise()
        break
    elif choose == "注销账号":
        cancel()
        break
    elif choose == "退出系统":
        break
    else:
        print("\033[31;40m并没有该选项\033[0m")
