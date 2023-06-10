from pathlib import Path

while True:
    folder = input("文件夹:")
    folder = Path(folder.strip())
    if folder.exists() and folder.is_dir():
        break
    else:
        print("不正确")
keyword = input("名称:").strip()
result = list(folder.rglob(f'*{keyword}*'))
if len(result) == 0:
    print(f'【{folder}】下无【{keyword}】文件或文件夹:')
else:
    result_folder = []
    result_file = []
    for i in result:
        if i.is_dir():
            result_folder.append(i)
        else:
            result_file.append(i)
    if len(result_folder) != 0:
        print(f'【{folder}】下【{keyword}】的文件夹:')
        for each in result_folder:
            print(each)
    if len(result_file) != 0:
        print(f'【{folder}】下【{keyword}】的文件:')
        for item in result_file:
            print(item)
