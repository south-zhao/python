import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import warnings
import numpy as np

warnings.filterwarnings("ignore")

df2_1 = pd.read_excel("附件2：302家无信贷记录企业的相关数据.xlsx", sheet_name="企业信息")
df2_2 = pd.read_excel("附件2：302家无信贷记录企业的相关数据.xlsx", sheet_name="进项发票信息")
df2_3 = pd.read_excel("附件2：302家无信贷记录企业的相关数据.xlsx", sheet_name="销项发票信息")

id2_to = list(df2_1["企业代号"])
id20 = []
id21 = []
for i in id2_to:
    # 获取总次数
    df1_31 = df2_3[df2_3["企业代号"] == i]
    total = df1_31.count()[0]
    ok_num = df1_31[(df1_31["发票状态"] == "有效发票") & (df1_31["金额"] >= 0)].count()[0] / total
    fu_num = df1_31[(df1_31["发票状态"] == "有效发票") & (df1_31["金额"] < 0)].count()[0] / total
    not_num = df1_31[df1_31["发票状态"] == "作废发票"].count()[0] / total
    money_avg = df1_31[df1_31["金额"] >= 0]["金额"].sum() / total
    not_num1 = df1_31[(df1_31["发票状态"] == "作废发票") & (df1_31["金额"] == 0)].count()[0] / total
    if not_num1 > 0.05:
        id20.append(i)
    else:
        id21.append(i)


# 获取企业代号
def new_data1(id0, name):
    # 每个企业对应的进项发票各类状态占比
    in_ok = []  # 有效占比
    in_fu = []  # 负数占比
    in_not = []  # 作废占比
    in_count = []  # 次数
    in_money = []  # 金额/次
    for i in id0:
        # 获取总次数
        df1_21 = df2_2[df2_2["企业代号"] == i]
        total = df1_21.count()[0]
        ok_num = df1_21[(df1_21["发票状态"] == "有效发票") & (df1_21["金额"] >= 0)].count()[0] / total
        fu_num = df1_21[(df1_21["发票状态"] == "有效发票") & (df1_21["金额"] < 0)].count()[0] / total
        not_num = df1_21[df1_21["发票状态"] == "作废发票"].count()[0] / total
        money_avg = df1_21[df1_21["金额"] >= 0]["金额"].sum() / total
        in_ok.append(ok_num)
        in_fu.append(fu_num)
        in_not.append(not_num)
        in_count.append(total)
        in_money.append(money_avg)

    # 每个企业对应的销项发票各类状态占比
    out_ok = []  # 有效占比
    out_fu = []  # 负数占比
    out_not = []  # 作废占比
    out_count = []  # 次数
    out_money = []  # 金额
    for i in id0:
        # 获取总次数
        df1_31 = df2_3[df2_3["企业代号"] == i]
        total = df1_31.count()[0]
        ok_num = df1_31[(df1_31["发票状态"] == "有效发票") & (df1_31["金额"] >= 0)].count()[0] / total
        fu_num = df1_31[(df1_31["发票状态"] == "有效发票") & (df1_31["金额"] < 0)].count()[0] / total
        not_num = df1_31[df1_31["发票状态"] == "作废发票"].count()[0] / total
        money_avg = df1_31[df1_31["金额"] >= 0]["金额"].sum() / total
        out_ok.append(ok_num)
        out_fu.append(fu_num)
        out_not.append(not_num)
        out_count.append(total)
        out_money.append(money_avg)

    df_new = pd.DataFrame(
        {"企业代号": id0, "进项有效发票占比": in_ok, "进项作废发票占比": in_not, "进项负数发票占比": in_fu,
         "进项次数": in_count, "进项平均每次金额": in_money, "销项有效发票占比": out_ok, "销项作废发票占比": out_not,
         "销项负数发票占比": out_fu, "销项次数": out_count, "销项平均每次金额": out_money})
    df_new.to_csv(f"{name}.csv", index=False, sep=",")


def mein(data):
    data1 = np.array(data)
    data_new = []
    for i in data1:
        data_new.append(list(np.delete(i, 0)))
    data_new = np.array(data_new)

    # 对每一个属性的样本求均值
    MEAN = np.mean(data_new, axis=0)

    # 去中心化
    X = np.subtract(data_new, MEAN)

    # 计算协方差矩阵
    COV = np.dot(X.T, X)

    # 计算特征值和特征向量
    W, V = np.linalg.eig(COV)  # W特征值，V特征向量

    # 计算主成分贡献率以及累计贡献率
    sum_lambda = np.sum(W)  # 特征值的和

    f = np.divide(W, sum_lambda)  # 每个特征值的贡献率（特征值 / 总和）

    # 前两大特征值对应的特征向量为：
    e1 = V.T[0]
    e2 = V.T[1]

    # 计算主成分值（已去中心化）
    z1 = np.dot(X, e1)
    z2 = np.dot(X, e2)

    # 输出降维后的结果（已去中心化）
    RES = np.array([z1, z2])

    return RES.T




df1_1 = pd.read_excel("附件1：123家有信贷记录企业的相关数据.xlsx", sheet_name="企业信息")
df1_2 = pd.read_excel("附件1：123家有信贷记录企业的相关数据.xlsx", sheet_name="进项发票信息")
df1_3 = pd.read_excel("附件1：123家有信贷记录企业的相关数据.xlsx", sheet_name="销项发票信息")

id_to = list(df1_1["企业代号"])
id0 = []
id0_degree = []
id1 = []
id1_degree = []
for i in id_to:
    # 获取总次数
    df1_31 = df1_3[df1_3["企业代号"] == i]
    total = df1_31.count()[0]
    not_num1 = df1_31[(df1_31["发票状态"] == "作废发票") & (df1_31["金额"] == 0)].count()[0] / total
    degree = list(df1_1[df1_1["企业代号"] == i]["信誉评级"])
    if not_num1 > 0.05:
        id0.append(i)
        id0_degree.extend(degree)
    else:
        id1.append(i)
        id1_degree.extend(degree)


def new_data(id0, name):
    # 每个企业对应的进项发票各类状态占比
    in_ok = []  # 有效占比
    in_fu = []  # 负数占比
    in_not = []  # 作废占比
    in_count = []  # 次数
    in_money = []  # 金额/次
    for i in id0:
        # 获取总次数
        df1_21 = df1_2[df1_2["企业代号"] == i]
        total = df1_21.count()[0]
        ok_num = df1_21[(df1_21["发票状态"] == "有效发票") & (df1_21["金额"] >= 0)].count()[0] / total
        fu_num = df1_21[(df1_21["发票状态"] == "有效发票") & (df1_21["金额"] < 0)].count()[0] / total
        not_num = df1_21[df1_21["发票状态"] == "作废发票"].count()[0] / total
        money_avg = df1_21[df1_21["金额"] >= 0]["金额"].sum() / total
        in_ok.append(ok_num)
        in_fu.append(fu_num)
        in_not.append(not_num)
        in_count.append(total)
        in_money.append(money_avg)

    # 每个企业对应的销项发票各类状态占比
    out_ok = []  # 有效占比
    out_fu = []  # 负数占比
    out_not = []  # 作废占比
    out_count = []  # 次数
    out_money = []  # 金额
    for i in id0:
        # 获取总次数
        df1_31 = df1_3[df1_3["企业代号"] == i]
        total = df1_31.count()[0]
        ok_num = df1_31[(df1_31["发票状态"] == "有效发票") & (df1_31["金额"] >= 0)].count()[0] / total
        fu_num = df1_31[(df1_31["发票状态"] == "有效发票") & (df1_31["金额"] < 0)].count()[0] / total
        not_num = df1_31[df1_31["发票状态"] == "作废发票"].count()[0] / total
        money_avg = df1_31[df1_31["金额"] >= 0]["金额"].sum() / total
        out_ok.append(ok_num)
        out_fu.append(fu_num)
        out_not.append(not_num)
        out_count.append(total)
        out_money.append(money_avg)

    df_new = pd.DataFrame(
        {"企业代号": id0, "进项有效发票占比": in_ok, "进项作废发票占比": in_not, "进项负数发票占比": in_fu,
         "进项次数": in_count, "进项平均每次金额": in_money, "销项有效发票占比": out_ok, "销项作废发票占比": out_not,
         "销项负数发票占比": out_fu, "销项次数": out_count, "销项平均每次金额": out_money})
    df_new.to_csv(f"{name}.csv", index=False, sep=",")


new_data(id0, "整合数据1")
new_data(id1, "整合数据2")

# 得到初始数据
data = pd.read_csv("整合数据2.csv")

x0 = np.array(mein(data))

# 处理马氏 44
target = id1_degree

v = np.cov(x0.T)  # 计算协方差

knn = KNeighborsClassifier(4, metric='mahalanobis', metric_params={'V': v})  # 马氏距离分类

knn.fit(x0, target)

pre = knn.predict(x0)

data1 = pd.read_csv("整合数据1.csv")
x01 = np.array(mein(data1))

target1 = id0_degree

v1 = np.cov(x01.T)  # 计算协方差

knn1 = KNeighborsClassifier(4)  # 欧氏距离分类

knn1.fit(x01, target1)

pre1 = knn1.predict(x01)

new_data1(id20, "整合数据3")
new_data1(id21, "整合数据4")

data2 = pd.read_csv("整合数据3.csv")
x2 = np.array(mein(data2))

pre2 = knn1.predict(x2)

data3 = pd.read_csv("整合数据4.csv")
x21 = np.array(mein(data3))

pre21 = knn.predict(x21)

list21 = [[int(i[1:]), j] for i, j in zip(id20, pre2)]
list22 = [[int(i[1:]), j] for i, j in zip(id21, pre21)]
list21.extend(list22)
list21.sort()
value2 = [i[1] for i in list21]
df2_1.insert(2, column="判别归类", value=value2)
df2_1.to_csv("判别评级表.csv", index=False)

