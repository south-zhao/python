# 导入所需的库
import numpy as np
import matplotlib.pyplot as plt

# 定义SIR模型的参数
beta = 0.2969*1.25 # 感染率 隔离措施较为松时
beta1 = 0.2969*0.75 # 感染率 隔离措施较为严格
beta2 = 0.2969 # 感染率
gamma = 0.0234 # 恢复率
N = 1000000 # 总人口
I0 = 2 # 初始感染者
R0 = 0 # 初始康复者
S0 = N - I0 - R0 # 初始易感者

# 定义时间步长和总时长
dt = 1 # 时间步长
T = 100 # 总时长
t = np.arange(0, T+dt, dt) # 时间序列

# 定义SIR模型的微分方程
def SIR_model(beta, S, I, R):
    dS = -beta * S * I / N # 易感者的变化率
    dI = beta * S * I / N - gamma * I # 感染者的变化率
    dR = gamma * I # 康复者的变化率
    return dS, dI, dR

# 初始化S, I, R的数组
S = np.zeros(len(t))
I = np.zeros(len(t))
R = np.zeros(len(t))

S1 = np.zeros(len(t))
I1 = np.zeros(len(t))
R1 = np.zeros(len(t))

S2 = np.zeros(len(t))
I2 = np.zeros(len(t))
R2 = np.zeros(len(t))

# 设置初始值
S[0] = S0
I[0] = I0
R[0] = R0

S1[0] = S0
I1[0] = I0
R1[0] = R0

S2[0] = S0
I2[0] = I0
R2[0] = R0
# 用欧拉法求解微分方程
for i in range(1, len(t)):
    dS, dI, dR = SIR_model(beta, S[i-1], I[i-1], R[i-1])
    S[i] = S[i-1] + dS * dt
    I[i] = I[i-1] + dI * dt
    R[i] = R[i-1] + dR * dt

for i in range(1, len(t)):
    dS, dI, dR = SIR_model(beta1, S1[i-1], I1[i-1], R1[i-1])
    S1[i] = S1[i-1] + dS * dt
    I1[i] = I1[i-1] + dI * dt
    R1[i] = R1[i-1] + dR * dt
    
for i in range(1, len(t)):
    dS, dI, dR = SIR_model(beta2, S2[i-1], I2[i-1], R2[i-1])
    S2[i] = S2[i-1] + dS * dt
    I2[i] = I2[i-1] + dI * dt
    R2[i] = R2[i-1] + dR * dt

# 绘制S, I, R随时间的变化曲线
# plt.plot(t, S, label='Susceptible')
plt.plot(t, I, label='Infected 1.25')
plt.plot(t, I1, label='Infected1 0.75')
plt.plot(t, I2, label='Infected2 1')
plt.xlabel('Time')
plt.ylabel('Number of people')
plt.legend()
plt.show()