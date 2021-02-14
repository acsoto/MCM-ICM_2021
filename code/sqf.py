import pandas as pd
import numpy as np
import math
from numpy import array
import ast

df = pd.read_csv('full_music_data.csv')
df['artists_id'] = df['artists_id'].map(ast.literal_eval)  # 把字符串转为集合
df.drop(columns=['artist_names', 'explicit', 'release_date', 'song_title (censored)'], inplace=True)
# df.set_index(['artists_id'], inplace=True)
# data_by_artist_df_scale = (data_by_artist_df-data_by_artist_df.mean())/data_by_artist_df.std() #按人标准化
# data_by_artist_array_scale = data_by_artist_df_scale.values
#####################
artist_inf_df = pd.read_csv('ArtistsInf.csv')
artist_inf_df.drop(['Unnamed: 0'], axis=1, inplace=True)
artist_inf_df.drop([0], axis=0, inplace=True)
artist_inf_array = artist_inf_df.values
Artists = {}
for i in artist_inf_df.values:
    Artists[i[0]] = i.tolist()

# only pop/rock only in dict  筛选
FullMusicList = []
for i in df.values:
    id = str(i[0][0])
    year = i[14]
    if id in Artists.keys():
        if Artists[id][2] == 'Pop/Rock':
            i[0] = id
            FullMusicList.append(i.tolist())

# print(FullMusicList)

map2 = {}
choose3 = ['valence', 'danceability', 'duration_ms']
for year in range(1961,1971):
    list = []
    for a in FullMusicList:
        if a[14] == year:
            list.append([a[3], a[1], a[12]])
    map2[year] = pd.DataFrame(np.array(list)).mean().values
choose3df = pd.DataFrame(map2).T
choose3df.columns = choose3
# choose3df.to_csv('1961-1970.csv')

# 定义熵值法函数
def cal_weight(x):
    # '''熵值法计算变量的权重'''
    # 标准化
    x = x.apply(lambda x: ((x - np.min(x)) / (np.max(x) - np.min(x))))

    # 求k
    rows = x.index.size  # 行
    cols = x.columns.size  # 列
    k = 1.0 / math.log(rows)

    lnf = [[None] * cols for i in range(rows)]

    # 矩阵计算--
    # 信息熵

    x = array(x)
    lnf = [[None] * cols for i in range(rows)]
    lnf = array(lnf)
    for i in range(0, rows):
        for j in range(0, cols):
            if x[i][j] == 0:
                lnfij = 0.0
            else:
                p = x[i][j] / x.sum(axis=0)[j]
                lnfij = math.log(p) * p * (-k)
            lnf[i][j] = lnfij
    lnf = pd.DataFrame(lnf)
    E = lnf

    # 计算冗余度
    d = 1 - E.sum(axis=0)
    # 计算各指标的权重
    w = [[None] * 1 for i in range(cols)]
    for j in range(0, cols):
        wj = d[j] / sum(d)
        w[j] = wj
        # 计算各样本的综合得分,用最原始的数据

    w = pd.DataFrame(w)
    return w



StartYear = 2001
YearVectors = []
for i in range(2):
    StartYear += i*10
    vectors = []
    for year in range(StartYear, StartYear + 10):
        list = []
        for a in FullMusicList:
            if a[14] == year:
                list.append(a[1:14])
        if (len(list) != 0):
            vectors.append(pd.DataFrame(list).mean().values)
    sq = pd.DataFrame(np.array(vectors))
    # 计算df各字段的权重
    # print(df.drop(columns=['artists_id', 'year'])[1:5])
    # w = cal_weight(sq)  # 调用cal_weight
    # YearVectors.append(w.T.values[0])
    # w.index = df.drop(columns=['artists_id', 'year']).columns
    # w.columns = ['weight']
# csv = pd.DataFrame(YearVectors)
# csv.columns = df.drop(columns=['artists_id', 'year']).columns
# print(csv)


year = 1941
EveryVector = {}
for i in range(80):
    year = 1941 + i
    list = []
    for a in FullMusicList:
        if a[14] == year:
            list.append(a[1:14])
    if (len(list) != 0):
        EveryVector[year] = pd.DataFrame(list).mean().values.tolist()
df1 = pd.DataFrame(EveryVector).T
df1.columns = df.drop(columns=['artists_id', 'year']).columns
df1 = (df1 - df1.min())/(df1.max() - df1.min())
df1.to_csv('EveryYearVector.csv')
# print(np.array(EveryVector))