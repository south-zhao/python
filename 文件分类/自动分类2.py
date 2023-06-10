from pathlib import Path

src_folder = Path('D:\\大一下\\选修课\\')
des_folder = Path('D:\\大一下\\选修课\\说课')
files = src_folder.glob('*')
for i in files:
    if i.is_file():
        des_path = des_folder / i.suffix.strip('.')
        if not des_path.exists():
            des_path.mkdir(parents=True)
        i.replace(des_path / i.name)
