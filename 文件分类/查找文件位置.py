from pathlib import Path

while True:
    folder = input("磁盘和文件夹:")
    folder = Path(folder.strip())
    if folder.exists() and folder.is_dir():
        break
    else:
        print("不正确")
keyword = input("名称:").strip()
result = list(folder.rglob(keyword))
if len(result) != 0:
    print(f'【{folder}】下【{keyword}】:')
    for i in result:
        print(i)
else:
    print(f'【{folder}】下无【{keyword}】:')
