# print(Path.cwd())  # 输出当前文件夹的位置
# print(Path.home())  # 获取home目录
# print(Path.stat(Path.cwd()))  # 获取当前文件的信息
# p = Path().rglob('test1.py')  # 查找所有文件夹，全部
# p = Path().glob('test1.py')  # 只查看这一级的文件
# Path().is_dir()  # 判断是否为文件夹
# Path().is_file()  # 判断是否为文件
# path = Path.cwd().iterdir()  # 当path为文件夹时，通过yield产生path文件夹下的所有文件、文件夹路径的迭代器
# print(Path().read_text())  # 读取文件内容
# Path().open()  # 打开文件
# path = Path.cwd()/"pathlib  path模块.py"
# new = path.with_name('path模块.py')  #  重命名
# path.replace(new)
# txt_path = Path('archive/demo.txt')
# new_file = txt_path.with_suffix('.json')
# txt_path.replace(new_file)  # 修改后缀名
# path = Path.cwd()/"path模块.py"
# print(path.name)  # 文件名和后缀
# print(path.suffix)  # 后缀
# print(path.stem)  # 文件名不含后缀
# path = Path('C:/Users/赵鑫杰')
# path1 = path.rglob('模糊查找.py')
# for i in path1:
#     print(i)





























