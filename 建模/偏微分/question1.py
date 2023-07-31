# 导入必要的库
import numpy as np
import matplotlib.pyplot as plt


L = 0.007  # 纺织材料总厚度，单位m
dt1 = 0.01  # 时间步长，单位s
dx1 = 0.0001  # 空间步长，单位m
Nt1 = int(10 * 60 / dt1)  # 时间步数
Nx1 = int(L / dx1)  # 空间步数
r1 = dt1 / (dx1 * dx1)


# 定义人体皮肤温度和水蒸气浓度随时间变化的函数
def Ts(t):
    return 35.84 + np.exp(0.0002 * t)


def Cs(t):
    return 0.05 + 0.25 * t - 0.0001 * t * t


# 定义网格矩阵
U = np.ones((Nt1, Nx1))

x1, x2, x3 = 0.002, 0.004, 0.007

# 时间上初始化
for i in range(Nt1):
    U[:, 0][i] = Ts(i * dt1)


def ts(k1, k2, k3):
    for i in range(1, Nt1):
        for j in range(1, Nx1 - 1):
            if dx1 * j <= x1:
                U[i, j] = (U[i - 1, j - 1] * r1 - 2 * r1 * U[i - 1, j] + r1 * U[i - 1, j + 1]) * k1 + U[i - 1, j]
            elif x1 < dx1 * j <= x2:
                U[i, j] = k2 * (U[i - 1, j - 1] * r1 - 2 * r1 * U[i - 1, j] + r1 * U[i - 1, j + 1]) + U[i - 1, j]
            elif x2 < dx1 * j <= x3:
                U[i, j] = k3 * (U[i - 1, j - 1] * r1 - 2 * r1 * U[i - 1, j] + r1 * U[i - 1, j + 1]) + U[i - 1, j]

    plt.figure()
    ax1 = plt.axes(projection='3d')
    x = np.arange(0, 0.007, dx1)
    y = np.arange(0, 600, dt1)
    X, Y = np.meshgrid(x, y)
    ax1.plot_surface(X, Y, U, cmap='rainbow')
    ax1.set_xlabel('X(/m)')
    ax1.set_ylabel('t(/s)')
    ax1.set_zlabel('T(/C)')
    plt.show()
    return U


dt = 0.001  # 时间步长，单位s

dx = 0.001  # 空间步长，单位m
Nt = int(10 * 60 / dt) + 1  # 时间步数
Nx = int(L / dx) + 1  # 空间步数
r = dt / (dx * dx)


def cs(d1, d3, q1, q3, s1, s2, s3, z1, z2, z3):
    C = np.full((Nt, Nx), 0.05 * d3 / s3 / q3)

    for i in range(Nt):
        C[:, 0][i] = Cs(i * dt) * d1 / s1 / q1

    for i in range(1, Nt):
        for j in range(1, Nx - 1):
            if dx * j <= x1:
                C[i, j] = (C[i - 1, j - 1] * r - 2 * r * C[i - 1, j] + r * C[i - 1, j + 1]) * 0.0000249 * s1 / z1 + C[
                    i - 1, j]
            elif x1 < dx * j <= x2:
                C[i, j] = 0.0000249 * (C[i - 1, j - 1] * r - 2 * r * C[i - 1, j] + r * C[i - 1, j + 1]) * s2 / z2 + C[
                    i - 1, j]
            elif x2 < dx * j <= x3:
                C[i, j] = 0.0000249 * (C[i - 1, j - 1] * r - 2 * r * C[i - 1, j] + r * C[i - 1, j + 1]) * s3 / z3 + C[
                    i - 1, j]

    plt.figure()
    ax2 = plt.axes(projection='3d')
    x = np.arange(0, 0.008, dx)
    y = np.arange(0, 600.001, dt)
    X, Y = np.meshgrid(x, y)
    ax2.plot_surface(X, Y, C, cmap='rainbow')
    ax2.set_xlabel('X')
    ax2.set_ylabel('t')
    ax2.set_zlabel('c(e-6)')
    plt.show()
    return C


# 第一个
U1 = ts(0.541 / (1540 * 1210), 0.58 / (1540 * 1210), 0.5 / (1380 * 1340))
C1 = cs(0.17, 0.10, 3552900, 2522000, 0.95, 0.95, 0.98, 1.455, 1.455, 1.476)

# 第二个
U2 = ts(0.385 / (1300 * 1360), 0.541 / (1540 * 1210), 0.5 / (1380 * 1340))
C2 = cs(0.137, 0.10, 4124500, 2522000, 0.925, 0.95, 0.98, 1.433, 1.455, 1.476)

# 第三个
U3 = ts(0.385 / (1300 * 1360), 0.58 / (1540 * 1210), 0.5 / (1380 * 1340))
C3 = cs(0.137, 0.10, 4124500, 2522000, 0.925, 0.95, 0.98, 1.433, 1.455, 1.476)
