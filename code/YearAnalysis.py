import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

#############
# 构造艺术家字典
ArtistsMap = {}
data_by_artist_df = pd.read_csv("data_by_artist.csv")
for index, row in data_by_artist_df.iterrows():
    ArtistsMap[str(row[1])] = index
print("艺术家索引表构造完毕")
data_by_artist_df.drop(columns=['artist_name', 'count'], inplace=True)
data_by_artist_df.set_index(["artist_id"], inplace=True)
data_by_artist_df_scale = (data_by_artist_df-data_by_artist_df.mean())/data_by_artist_df.std() #按人标准化
data_by_artist_array_scale = data_by_artist_df_scale.values
################### year
data_by_year_df = pd.read_csv("data_by_year.csv")
# data_by_year_df.drop('mode', axis=1, inplace=True)  #按年标准化需要去除mode
data_by_year_df.set_index('year', inplace=True)
data_by_year_df_scale = (data_by_year_df-data_by_artist_df.mean())/data_by_artist_df.std() #按人标准化
data_by_year_array_scale = data_by_year_df_scale.values
###################
artist_inf_df = pd.read_csv('ArtistsInf.csv')
artist_inf_df.drop(['Unnamed: 0'], axis=1, inplace=True)
artist_inf_df.drop([0], axis=0, inplace=True)
artist_inf_array = artist_inf_df.values


# 提取到array

def FixCosSimilarity(p1, p2, dimension):
    mean1 = np.mean(p1)
    mean2 = np.mean(p2)
    fixed1 = [p1[x] - mean1 for x in range(dimension)]
    fixed2 = [p2[x] - mean2 for x in range(dimension)]
    return cosine_similarity([fixed1], [fixed2])[0][0]



# 计算年间相似度
# Similarity_year_by_year = {}
# list = []
# for i in range(99):
#     list.append(FixCosSimilarity(data_by_year_array[i], data_by_year_array[i + 1], 12))
# df = pd.DataFrame(list)
# df = (df - df.min()) / (df.max() - df.min())
# for i in range(99):
#     Similarity_year_by_year[str(i + 1921) + '-' + str(i + 1922)] = df.values[i]
# pd.DataFrame(Similarity_year_by_year).to_csv('Similarity_year_by_year.csv')


list = []
for i in artist_inf_array:
    if i[3] == '1970' or i[3] == '1980':
        list.append(i.tolist())

list = sorted(list, key=lambda x: float(x[4]), reverse=True)
list = list[0:10]
print("艺术家影响力top10")
minsim = 10
maxsim = -10
list1 = []
for i in list:
    index = ArtistsMap[i[0]]
    index_year = 1981 - 1921
    simi = FixCosSimilarity(data_by_artist_array_scale[index], data_by_year_array_scale[index_year], 13)
    if simi<minsim : minsim = simi
    if simi>maxsim : maxsim = simi
    i.append(simi)
for i in list:
    print(i[1], i[4], (i[5]-minsim)/(maxsim-minsim))
