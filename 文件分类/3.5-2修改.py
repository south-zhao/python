import pandas as pd


a = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=['data', 'score'], index=['A', 'B', 'C'])
a.index.name = '公司'
a = a.rename(index={'A': '万科', 'B': '阿里', 'C': '百度'}, columns={'data': '日期', 'score': '分数'})
a = a.reset_index()
print(a)
