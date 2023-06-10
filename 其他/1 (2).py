import time


def main():
    print(time.time())
    print(time.localtime())
    print(time.gmtime())
    print(time.strftime('%a,%d %b %Y %H:%M:%S'))
    print(time.asctime())
    print(time.ctime())  # 与asctime相似
    print(time.strptime('Sat,14 May 2022 21:44:32', '%a,%d %b %Y %H:%M:%S'))
    print("开始")
    time.sleep(3.5)  # 停止一段时间
    print('结束')


if __name__ == "__main__":
    main()
