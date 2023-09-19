"""
    C:\\Bin\\environment\\python
    -*- coding: utf-8 -*-
    @Time :  2023/9/13 16:33
    @Author : south(南风)
    @File : 数独.py
    Describe:
    -*- coding: utf-8 -*-
"""
import numpy as np


def sudoku_solve(N=9, input=None):
    def get_possible(MM, row, col):
            # 行列上的各个值
        t = np.unique(np.append(MM[row, :], MM[:, col]))
        t1 = MM[int(row/3)*3: int(row/3)*3+3, int(col/3)*3: int(col/3)*3+3]
        tt1 = np.append(t1[0], t1[1])
        tt1 = np.append(tt1, t1[2])
        tt1 = np.setdiff1d(ONE_N, tt1)
        t = np.setdiff1d(ONE_N, t)  # 集合的差
        t = np.intersect1d(t, tt1)
        return t

    def isdone(MM):
        if MM is None:
            return False

        for row in range(N):
            if not np.all(ONE_N == np.sort(MM[row, :])):
                return False
            if not np.all(ONE_N == np.sort(MM[:, row])):
                return False
        return True

    def islegal(MM):
        for ind in range(N):  # 判断所有行列是否合法
            t = MM[ind, :]
            t = t[t > 0]
            tt = np.unique(t)
            if t.size != tt.size:  # 有重复元素
                return False
            t = MM[:, ind]  # 列
            t = t[t > 0]
            tt = np.unique(t)
            if t.size != tt.size:  # 有重复元素
                return False
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                t = MM[i:i + 3, j:j + 3]
                t1 = np.append(t[0], t[1])
                t1 = np.append(t1, t[2])
                t1 = t1[t1 > 0]
                tt = np.unique(t1)
                if t1.size != tt.size:
                    return False
        return True

    def findsmallest(MM):
        sm = np.inf
        a = None
        b = None
        for ii in range(N):
            for jj in range(N):
                if MM[ii, jj] == 0:
                    t = get_possible(MM, ii, jj)
                    if t.size < sm:
                        sm = t.size
                        a = ii
                        b = jj
        if sm == 0:
            return None, None
        return a, b

    def set1(MM):
        done = True
        while done:
            done = False
            for ii in range(N):
                for jj in range(N):
                    if MM[ii, jj] == 0:
                        t = get_possible(MM, ii, jj)
                        if t.size == 1:
                            MM[ii, jj] = t
                            done = True
        return MM

    def sudoku(M):
        MM = M.copy()
        MM = set1(MM)

        if isdone(MM):
            return MM

        if not islegal(MM):
            return None

        a, b = findsmallest(MM)
        if a is None:
            return None
        t = get_possible(MM, a, b)  # 可能:
        for ii in range(t.size):
            MM[a, b] = t[ii]
            Mtemp = sudoku(MM)
            if Mtemp is None:
                continue
            else:
                if isdone(Mtemp):
                    return Mtemp
        return None


    ONE_N = np.arange(N) + 1

    return sudoku(input)


# input = np.array([[8, 0, 0, 0, 0, 0, 0, 0, 0],
#                   [0, 0, 3, 6, 0, 0, 0, 0, 0],
#                   [0, 7, 0, 0, 9, 0, 2, 0, 0],
#                   [0, 5, 0, 0, 0, 7, 0, 0, 0],
#                   [0, 0, 0, 0, 4, 5, 7, 0, 0],
#                   [0, 0, 0, 1, 0, 0, 0, 3, 0],
#                   [0, 0, 1, 0, 0, 0, 0, 6, 8],
#                   [0, 0, 8, 5, 0, 0, 0, 1, 0],
#                   [0, 9, 0, 0, 0, 0, 4, 0, 0]])

input = np.array([[0, 0, 5, 3, 0, 0, 0, 0, 0],
                  [8, 0, 0, 0, 0, 0, 0, 2, 0],
                  [0, 7, 0, 0, 1, 0, 5, 0, 0],
                  [4, 0, 0, 0, 0, 5, 3, 0, 0],
                  [0, 1, 0, 0, 7, 0, 0, 0, 6],
                  [0, 0, 3, 2, 0, 0, 0, 8, 0],
                  [0, 6, 0, 5, 0, 0, 0, 0, 9],
                  [0, 0, 4, 0, 0, 0, 0, 3, 0],
                  [0, 0, 0, 0, 0, 9, 7, 0, 0]])


print(sudoku_solve(input=input))
