# -*- coding: utf-8 -*-
# @Time : 2022/8/20 20:49
# @Author : south(南风)
# @File : Bank.py
# Describe:
# -*- coding: utf-8 -*-
# 银行功能
import os
import time
import json


class Bank:
    def __init__(self):
        account1 = input("请输入账号:").strip()
        password1 = input("请输入密码:").strip()
        txt_name = os.path.join(os.getcwd(), "user_information", f"{account1}")
        with open(txt_name, 'r', encoding="utf-8") as f:
            dict1 = json.load(f)
        if account1 == dict1['account'] and password1 == dict1['password']:
            self.name = txt_name
            self.account = account1
            self.password = password1
            self.num = dict1['money']
            self.flow = dict1['flow']
            self.check = True
        else:
            print("账号错误")
            self.check = False
            return

    def save(self):
        num1 = input("输入你要存钱的数目:").strip()
        self.num += int(num1)
        time1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())   # time1 = time.asctime(time.localtime())
        flow1 = f"存入{num1}元, 余额为{self.num}元"
        dict2 = {time1: flow1}
        self.flow.update(dict2)
        Bank.keep(self)

    def get(self):
        num2 = input("输入你要取钱的数目:").strip()
        self.num -= int(num2)
        time1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # time1 = time.asctime(time.localtime())
        flow1 = f"取出{num2}元, 余额为{self.num}元"
        dict2 = {time1: flow1}
        self.flow.update(dict2)
        Bank.keep(self)

    def re_print(self):
        check = {
            "1": self.num,
            '2': self.flow
        }
        a = """        ------------
        | 1.金额    |
        | 2.流水    |
        ------------"""
        print(a)
        chose = input("输入查看的选项:").strip()
        if chose == "2":
            print("想查看全部账单输入1，查看部分账单输入2:")
            re_chose = input().strip()
            if re_chose == "1":
                for i in self.flow:
                    print(i, ":", self.flow[i])
            else:
                check_time = input("输入你想查看的开始时间:").strip()
                for i in self.flow:
                    if time.mktime(time.strptime(i, "%Y-%m-%d %H:%M:%S")) > time.mktime(time.strptime(check_time, "%Y-%m-%d")):
                        print(i, ":", self.flow[i])
        else:
            print(check[chose])

    def keep(self):
        dict1 = {
            "account": self.account,
            "password": self.password,
            "money": self.num,
            "flow": self.flow
        }
        with open(self.name, 'w', encoding="utf-8") as f:
            json.dump(dict1, f, ensure_ascii=False)


def register():
    account1 = input("请输入账号:").strip()
    password1 = input("请输入密码:").strip()
    re_password = input("请再次输入密码:").strip()
    txt_name = os.path.join(os.getcwd(), "user_information", f"{account1}")
    if password1 == re_password:
        dict1 = {
            "account": account1,
            "password": password1,
            "money": 0,
            "flow": {"2022-04-21 18:20:02": "存入20000元", "2022-10-21 18:20:02": "取出2000元"}
        }
        with open(txt_name, 'w', encoding="utf-8") as f:
            json.dump(dict1, f, ensure_ascii=False)


if __name__ == '__main__':
    while True:
        print("""----------
|1.注册    |
|2.登录    |
|3.退出    |
---------""")
        choose = input("请输入功能对应的数字:").strip()
        if choose == '1':
            register()
        elif choose == '2':
            user = Bank()
            while user.check:
                print("""----------
|1.存钱    |
|2.取钱    |
|3.打印账单 |
|4.退出    |
---------""")
                func1 = {
                    "1": user.save,
                    "2": user.get,
                    "3": user.re_print
                }
                num = input("输入你的选项:").strip()
                if num == "4":
                    break
                else:
                    func1[num]()
        else:
            print("退出")
            break










