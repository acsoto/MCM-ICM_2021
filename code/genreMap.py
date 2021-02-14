import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib import cm
from palettable.colorbrewer.qualitative import Pastel1_7

#############
from sklearn.metrics.pairwise import cosine_similarity

# SimFrame = pd.read_csv("Similarity.csv")
# SimFrame.drop(['Unnamed: 0'], axis=1, inplace=True)
# SimArray = SimFrame.values
# print("相似度矩阵读取完毕")
#############
# 构造艺术家字典
ArtistsMap = {}
data_by_artist_df = pd.read_csv("data_by_artist.csv")
for index, row in data_by_artist_df.iterrows():
    ArtistsMap[str(row[1])] = index
print("艺术家索引表构造完毕")
###################
df = pd.read_csv('ArtistsInf.csv')
df.drop(['Unnamed: 0'], axis=1, inplace=True)
df.drop([0], axis=0, inplace=True)
array = df.values
# 提取到array
GenreMap = {}
GenreSimilarity = {}

for row in array:
    if row[2] not in GenreMap.keys():
        list = [row.tolist()]
        GenreMap[row[2]] = list
    else:
        GenreMap[row[2]].append(row.tolist())
print('GenreMap 生成完毕')

YearMap = {}

for row in array:
    if row[3] not in YearMap.keys():
        list = [row.tolist()]
        YearMap[row[3]] = list
    else:
        YearMap[row[3]].append(row.tolist())
print('YearMap 生成完毕')


data_by_artist_df.drop(columns=['artist_name', 'count'], inplace=True)
data_by_artist_df.set_index(["artist_id"], inplace=True)
data_by_artist_df_scale = (data_by_artist_df-data_by_artist_df.mean())/data_by_artist_df.std() #标准化
data_by_artist_array_scale = data_by_artist_df_scale.values
print('13维标准化表生成完毕')


# 计算平均相似度
# for genere in GenreMap:
#     count = 0
#     c = 0
#     for i in GenreMap[genere]:
#         for j in GenreMap[genere]:
#             index1 = ArtistsMap[i[0]]
#             index2 = ArtistsMap[j[0]]
#             if index1 < index2:
#                 count += SimArray[index1][index2]
#                 c += 1
#     GenreSimilarity[genere] = count/c
#
# pd.DataFrame([GenreSimilarity]).to_csv('GenreSimilarity.csv')

# 计算总影响力
# GenreInfluence = {}
# for genere in GenreMap:
#     count = 0
#     for i in GenreMap[genere]:
#         count += float(i[4])
#     GenreInfluence[genere] = count
#
# pd.DataFrame([GenreInfluence]).to_csv('GenreInfluence.csv')

# 计算每个派别的平均向量
# GenreVector = {}
# for genere in GenreMap:
#     list = []
#     for i in GenreMap[genere]:
#         index = ArtistsMap[i[0]]
#         list.append(data_by_artist_array_scale[index].tolist())
#     one_df = pd.DataFrame(list)
#     GenreVector[genere] = one_df.mean().values
# pd.DataFrame(GenreVector).to_csv('GenreVector.csv')

def FixCosSimilarity(p1, p2):
    mean1 = np.mean(p1)
    mean2 = np.mean(p2)
    fixed1 = [p1[x]-mean1 for x in range(13)]
    fixed2 = [p2[x]-mean2 for x in range(13)]
    return cosine_similarity([fixed1], [fixed2])[0][0]


# RelevanceMat = np.zeros(shape=(20, 20))
# minSim = 0
# maxSim = 0
# i=j=-1
# for key1 in GenreMap:
#     i+=1
#     j=-1
#     for key2 in GenreMap:
#         j+=1
#         temp = FixCosSimilarity(GenreVector[key1], GenreVector[key2])
#         if(i<j):
#             RelevanceMat[i][j] = temp
#             if temp > maxSim:
#                 maxSim = temp
#             if temp < minSim:
#                 minSim = temp
# RelevanceFrame = pd.DataFrame(RelevanceMat)
# RelevanceFrame = (RelevanceFrame-minSim)/(maxSim-minSim)
# RelevanceFrame.index(GenreMap.keys())
# RelevanceFrame.columns(GenreMap.keys())
# RelevanceFrame.to_csv("GenreSimilarityMatrix.csv")


# 计算每年的平均向量

YearVector = {}
for year in YearMap:
    list = []
    for i in YearMap[year]:
        index = ArtistsMap[i[0]]
        list.append(data_by_artist_array_scale[index].tolist())
    one_df = pd.DataFrame(list)
    YearVector[year] = one_df.mean().values
# pd.DataFrame(YearVector).to_csv('YearVector.csv')


# 计算每年平均风格和该年平均风格最相似的流派

# def CalOneGenreYearVector (genre, year):
#     list = []
#     for i in GenreMap[genre]:
#         if i[3] == year:
#             index = ArtistsMap[i[0]]
#             list.append(data_by_artist_array_scale[index].tolist())
#     one_df = pd.DataFrame(list)
#     return one_df.mean().values
#
# GenreSimiByYear = {}
#
# for year in YearMap:
#     map = {}
#     for genre in GenreMap:
#         vec = CalOneGenreYearVector(genre, year)
#         if len(vec) != 0:
#             simi = FixCosSimilarity(vec, YearVector[year])
#             map[genre] = simi
#     # sorted_list = sorted(list, key=lambda x: x.simi, reverse=True)
#     GenreSimiByYear[year] = map
#
# # BestGenreByYear_df = {}
# # for year in BestGenreByYear:
# #     map = {}
# #     top = 0
# #     for i in BestGenreByYear[year]:
# #         top+=1
# #         map[top] = i.simi
# #     BestGenreByYear_df[year] = map
# pd.DataFrame(GenreSimiByYear).to_csv('GenreSimiByYear.csv')


