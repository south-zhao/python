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
        if MM[row, col] > 0:
            return MM[row, col]
        else:
            # 行列上的各个值
            t = np.unique(np.append(MM[row, :], MM[:, col]))
            t = np.setdiff1d(ONE_N, t)  # 集合的差
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
            if isdone(Mtemp):
                return Mtemp
        return MM

    # M = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
    #              [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #              [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #              [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #              [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #              [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #              [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #              [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #              [0, 0, 0, 0, 0, 0, 0, 0, 0]])
    ONE_N = np.arange(N) + 1

    # if input is not None:
    #     for row, col, v in input:
    #         M[row][col] = v

    return sudoku(input)


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

