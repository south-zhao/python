import pandas as pd

df = pd.read_excel("表1 指导教师信息与选队意愿.xls")
df = df.iloc[1:36]

df2 = pd.read_excel("表2 建模队信息与选择指导教师意愿.xls")
df2 = df2.iloc[2:177]
# 读取信息
df_in1 = pd.read_excel("表1 指导教师信息与选队意愿(2).xls")
df_in = df_in1.iloc[1:36, 9].values


def paiming(data1, data2, data3, num):
    list_p1 = data1.split("/")
    list_p2 = data2.split("/")
    list_p3 = data3.split("/")
    num = int(num)
    if int(list_p1[1]) * num / 100 > int(list_p1[0]) and int(list_p2[1]) * num / 100 > int(list_p2[0]) and int(
            list_p3[1]) * num / 100 > int(list_p3[0]):
        return True
    else:
        return False


def num_c(data1, data2, data3):
    num1 = 0
    if data1 == "2":
        num1 += 1
    if data2 == "2":
        num1 += 1
    if data3 == "2":
        num1 += 1
    return num1;


list_total = []
for i in df_in:
    list_t = []
    list_infor = i.split(",")
    for j in df2.values:
        num = 0
        if list_infor[0] == "D":
            if j[3] != j[9] != j[15]:
                num += 2
        if int(j[5]) + int(j[11]) + int(j[17]) == int(list_infor[1]):
            num += 2
        if list_infor[2] == "0":
            num += 2
        else:
            if paiming(j[6], j[12], j[18], list_infor[2]):
                num += 2
        if list_infor[3] == "无":
            num += 2
        else:
            listname = [j[3], j[9], j[15]]
            li = list_infor[3].split("、")
            if len(li) == 2:
                if li[0] in listname or li[1] in listname:
                    num += 2
            if len(li) == 3:
                if li[0] in listname or li[1] in listname or li[2] in listname:
                    num += 2
        num_co = num_c(j[4], j[10], j[16])
        if num_co >= int(list_infor[4]):
            num += 2
        list_t.append(num)
    list_total.append(list_t)
df_stu1 = pd.read_excel("表2 建模队信息与选择指导教师意愿(1).xls")
df_stu = df_stu1.iloc[2:177, 19].values


def compare(name, da):
    dict1 = {"教授": 2, "副教授": 1, "讲师": 0}
    num_l = dict1[name]
    num_p = dict1[da]
    if num_p > num_l:
        return True
    else:
        return False


list_total_st = []
for i in df_stu:
    list_teac = []
    list_s_infor = i.split("，")
    for j in df.values:
        num = 0
        if list_s_infor[0] == "无":
            num += 2.5
        else:
            if list_s_infor[0] == j[1]:
                num += 2.5
        if list_s_infor[1] == "无":
            num += 2.5
        else:
            if compare(list_s_infor[1], j[3]):
                num += 2.5
        if list_s_infor[2] == "无":
            num += 2.5
        else:
            if int(list_s_infor[2].split("年")[0]) <= int(j[6]):
                num += 2.5
        if list_s_infor[3] == "无":
            num += 2.5
        else:
            if "或" not in list_s_infor[3]:
                if j[5] == list_s_infor[3]:
                    num += 2.5
            else:
                o_name1 = list_s_infor[3].split("或")
                if j[5] in o_name1:
                    num += 2.5
        list_teac.append(num)
    list_total_st.append(list_teac)

level1 = [2, 7, 21, 29, 23, 17, 22]  # 7个   7个
level2 = [3, 9, 16, 28, 11, 8, 18, 32, 34, 25, 26]  # 11个    5个  前三6个
level3 = [13, 10, 12, 33, 1, 5, 6, 19, 31, 35, 14, 15, 20, 30, 4, 24, 27]  # 17个  4个

list_o = []

list_t_s = []

for i in range(1, 36):
    list_m = {}
    for j in range(1, 176):
        nu = list_total[i - 1][j - 1] * 0.5 + list_total_st[j - 1][i - 1] * 0.5
        list_m[str(j)] = nu
    list_t_s.append(list_m)

res = {}
for i in level1:
    l = []
    d_order = sorted(list_t_s[i - 1].items(), key=lambda x: x[1], reverse=True)
    j = 0
    num_i = 0
    while num_i <= 6:
        if d_order[j][0] not in list_t_s:
            list_o.append(d_order[j][0])
            l.append(d_order[j][0])
            num_i += 1
        j += 1
    res[str(i)] = l

for i in level2:
    l = []
    d_order = sorted(list_t_s[i - 1].items(), key=lambda x: x[1], reverse=True)
    j = 0
    num_i = 0
    if i in [3, 9, 16]:
        x = 5
    else:
        x = 4
    while num_i <= x:
        if d_order[j][0] not in list_t_s:
            list_o.append(d_order[j][0])
            l.append(d_order[j][0])
            num_i += 1
        j += 1
    res[str(i)] = l

for i in level3:
    l = []
    d_order = sorted(list_t_s[i - 1].items(), key=lambda x: x[1], reverse=True)
    j = 0
    num_i = 0
    while num_i <= 3:
        if d_order[j][0] not in list_t_s:
            list_o.append(d_order[j][0])
            l.append(d_order[j][0])
            num_i += 1
        j += 1
    res[str(i)] = l
print(res)
