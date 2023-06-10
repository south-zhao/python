import pandas as pd
import numpy as np

a = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=['data', 'score'], index=['A', 'B', 'C'])
print(a)


b = pd.DataFrame()
data = [1, 2, 3]
croce = [4, 5, 6]
b['data'] = data
b['croce'] = croce
print(b)


c = pd.DataFrame({'a': [1, 3, 5], 'b': [2, 4, 6]}, index=['x', 'y', 'z'])
print(c)


d = pd.DataFrame.from_dict({'a': [1, 2, 3], 'b': [4, 5, 6]}, orient='index')
print(d)

e = np.arange(12).reshape(3, 4)
f = pd.DataFrame(e, index=[1, 2, 3], columns=['A', 'B', 'C', 'D'])
print(f)
