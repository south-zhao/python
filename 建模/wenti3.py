# 导入需要的库
import numpy as np
import pandas as pd
from scipy.integrate import odeint
from scipy.optimize import minimize
import matplotlib.pyplot as plt
import requests
from lxml import etree


plt.rcParams['font.sans-serif']='SimHei'#设置中文显示
df = pd.read_excel("上海.xlsx")
url = "http://sh.bendibao.com/news/2020119/233243.shtm"
headers = {"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82"}

response = requests.get(url=url, headers=headers)

content = response.text

xml = etree.HTML(content)
to = [] # 总感染人数
local_y1 = []
da1 = []

for i in range(67, 250, 2):
    da1 = xml.xpath(f'/html/body/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[1]/table/tbody/tr[{i+1}]/td[3]//text()')
    loc_y1 = xml.xpath(f'/html/body/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[1]/table/tbody/tr[{i}]/td[4]//text()')
    
    if i == 115:
        da1[0]=570584
    to.append(int(da1[0])+int(loc_y1[0])) # 可能因为网络问题会报错，多运行几次就成功了

    
# 定义SIR模型的微分方程组
def sir_model(y, t, beta, gamma):
    S, I, R = y # y是一个包含S,I,R三个变量的向量
    dS_dt = -beta * S * I # 易感者的变化率
    dI_dt = beta * S * I - gamma * I # 感染者的变化率
    dR_dt = gamma * I # 康复者的变化率
    return [dS_dt, dI_dt, dR_dt] # 返回一个包含三个变化率的向量

# 定义初始条件
num2 = list(df["每日治愈人数"])[::-1]
rev = [] # 回复人数
for i in range(92):
    if i == 0:
        rev.append(num2[0])
    else:
        rev.append(rev[i-1]+num2[i])
N = 1000000 # 总人口数，单位：人
I0 = 2 / N # 初始感染者比例，单位：无量纲
R0 = 9 / N # 初始康复者比例，单位：无量纲
S0 = 1 - I0 - R0 # 初始易感者比例，单位：无量纲
y0 = [S0, I0, R0] # 初始条件向量
t = np.arange(1, len(rev) + 1) # 时间范围，单位：天

# 使用scipy.integrate.odeint()函数求解微分方程组，得到S,I,R随时间变化的数值解。
# 这里先假设beta和gamma为任意值，后面再用最优化方法求解它们。
beta = 0.01 # 传染率，单位：无量纲
gamma = 0.001 # 恢复率，单位：无量纲
solution = odeint(sir_model, y0, t, args=(beta, gamma)) # 求解微分方程组，返回一个二维数组，每一行对应一个时间点，每一列对应一个变量
solution = np.array(solution) # 将结果转换为numpy数组

# 定义损失函数，如最小二乘法，用来衡量模型预测的I和R与实际数据的差异。
def loss(point, N):
    size = len(rev)
    beta, gamma = point # point是一个包含beta和gamma的向量
    solution = odeint(sir_model, y0, t, args=(beta, gamma)) # 求解微分方程组
    solution = np.array(solution) # 转换为numpy数组
    pred_I = solution[:,1] * N # 预测的感染者人数，乘以总人口数N得到绝对值
    pred_R = solution[:,2] * N # 预测的康复者人数，乘以总人口数N得到绝对值
    real_I = np.array(to[::-1]) # 实际的感染者人数
    real_R = np.array(rev) # 实际的康复者人数
    error_I = np.mean((pred_I - real_I) ** 2) # 预测和实际的感染者人数的均方误差
    error_R = np.mean((pred_R - real_R) ** 2) # 预测和实际的康复者人数的均方误差
    error = error_I + error_R # 总的误差
    return error # 返回误差

# 使用scipy.optimize.minimize()函数寻找最优的beta和gamma参数，使得损失函数最小。
# 这里使用了L-BFGS-B算法，它是一种基于梯度的最优化方法，适用于有界约束的问题。
# 我们假设beta和gamma的取值范围都在0到1之间，作为约束条件。
optimal = minimize(loss, [beta, gamma], args=(N), method="L-BFGS-B", bounds=[(0, 1), (0, 1)]) # 求解最优化问题，返回一个OptimizeResult对象
beta, gamma = optimal.x # optimal.x是一个包含最优beta和gamma的向量
print(f"最优的传染率为{beta:.4f}，最优的恢复率为{gamma:.4f}") # 打印结果 # 最优的传染率为0.2969，最优的恢复率为0.0234

# 使用matplotlib.pyplot库绘制S,I,R随时间变化的曲线图，并与实际数据进行对比。
solution = odeint(sir_model, y0, t, args=(beta, gamma)) # 使用最优参数重新求解微分方程组
solution = np.array(solution) # 转换为numpy数组
plt.figure(figsize=(10, 6)) # 创建一个画布，设置大小为10*6英寸
plt.plot(t, np.array(to[::-1])-np.array(rev), "r", label="实际感染者") # 绘制实际感染者人数随时间变化的折线图，颜色为红色，标签为"实际感染者"
plt.plot(t, rev, "g", label="实际康复者") # 绘制实际康复者人数随时间变化的折线图，颜色为绿色，标签为"实际康复者"
plt.plot(t, solution[:,1] * N-solution[:,2] * N, "r--", label="预测感染者") # 绘制预测感染者人数随时间变化的折线图，颜色为红色，线型为虚线，标签为"预测感染者"
plt.plot(t, solution[:,2] * N, "g--", label="预测康复者") # 绘制预测康复者人数随时间变化的折线图，颜色为绿色，线型为虚线，标签为"预测康复者"
plt.xlabel("日期") # 设置x轴标签为"日期"
plt.ylabel("人数") # 设置y轴标签为"人数"
# plt.xticks(t[::10], data["date"][::10].dt.strftime("%m-%d"), rotation=45) # 设置x轴刻度为每10天一个日期，格式为"月-日"，旋转45度
plt.legend() # 显示图例
plt.title("SIR模型拟合") # 设置标题为"SIR模型拟合中国新冠疫情数据"
plt.show() # 显示图像