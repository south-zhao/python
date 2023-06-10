from pathlib import Path

src_file = Path('E:\\')
res = list(src_file.glob('*'))
res1 = list(src_file.rglob('*'))
for i in res:
    print(i)
print("----------------------------------------")
for i in res1:
    print(i)
