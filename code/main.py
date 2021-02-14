import pandas as pd
import csv
import numpy as np
import sys
import matplotlib.pyplot as plt
import json

# reader = pd.read_csv('influence_data.csv', encoding='UTF-8')
# df = pd.DataFrame(data)


class Artist:
    def __init__(self, id, name, genre, year):
        self.id = id
        self.name = name
        self.genre = genre
        self.year = year
        self.impact = []
        self.influence = 0


#############
SimFrame = pd.read_csv("Similarity.csv")
SimFrame.drop(['Unnamed: 0'], axis=1, inplace=True)
SimArray = SimFrame.values
print("相似度矩阵读取完毕")
#############
# 构造艺术家字典
ArtistsMap = {}
data_by_artist_df = pd.read_csv("data_by_artist.csv")
for index, row in data_by_artist_df.iterrows():
    ArtistsMap[str(row[1])] = index
print("艺术家索引表构造完毕")
data_by_artist_df.drop(columns=['artist_name', 'count'], inplace=True)
data_by_artist_df.set_index(["artist_id"], inplace=True)
data_by_artist_array = data_by_artist_df.values
print('13维表生成完毕')
#############
# 全局变量
Artists = {}
INFLUENCE_DECAY_FACTOR = 0.1
edges = []


def getSim(a1id, a2id):
    a1index = ArtistsMap[a1id]
    a2index = ArtistsMap[a2id]
    if a1index < a2index:
        return SimArray[a1index][a2index]
    else:
        return SimArray[a2index][a1index]

def getInfluence(artist):
    visited = {}
    for key in Artists:
        visited[key] = 0
    return CalInfluence(artist, visited)


def CalInfluence(artist, visited):
    visited[artist.id] = 1
    if len(artist.impact) == 0:
        return 0
    else:
        count = 0
        for sub in artist.impact:
            if visited[sub] == 0:
                if Artists[sub].year >= artist.year:
                    sim = getSim(artist.id, sub)
                    ###
                    # if (artist.id+"-"+sub) not in edges:
                        # edges.append(artist.id+"-"+sub)
                        # InfuList.append(sim)
                        # 边上的相似性加入集合
                        # pearX.append(getVector(artist.id))
                        # pearY.append(getVector(sub))
                        # 把向量加入集合
                    ###
                    count += sim * CalInfluence(Artists[sub], visited)
    return len(artist.impact) + INFLUENCE_DECAY_FACTOR * count

def getVector(id):
    index = ArtistsMap[id]
    return data_by_artist_array[index]


csvFile = open("influence_data.csv", "r", encoding='UTF-8')
reader = csv.reader(csvFile)

InfluenceList = [row for row in reader]
InfluenceList.remove(InfluenceList[0])

for row in InfluenceList:
    if row[4] != '477787':
        if row[0] not in Artists:
            a = Artist(row[0], row[1], row[2], row[3])
            Artists[row[0]] = a
        if row[4] not in Artists:
            b = Artist(row[4], row[5], row[6], row[7])
            Artists[row[4]] = b
        Artists[row[0]].impact.append(row[4])
print("艺术家字典构造完毕")


# for row in array:
#     count += 1
#     if count >= 500:
#         break
#     genre = row[2]
#     if genre not in GraphX:
#         GraphX.append(genre)
#         GraphY.append(1)
#     else:
#         index = GraphX.index(genre)
#         GraphY[index] += 1

# ArtistsCopy = Artists.copy()
# for k, v in Artists.copy().items():
#     if v.genre != 'Vocal':
#         Artists.pop(k)
#
# count = 0
# c = 0
# for key1 in Artists:
#     for key2 in Artists:
#         index1 = ArtistsMap[key1]
#         index2 = ArtistsMap[key2]
#         if(index1 < index2):
#             count += SimArray[index1][index2]
#             c += 1
# print(count/c)

InfuList = [] # 存放网络边上的相似性
pearX = [] # 网络边上的影响者向量集合
pearY = [] # 网络边上的被影响者向量集合


for key in Artists:
    Artists[key].influence = getInfluence(Artists[key])
print("艺术家影响力计算完成")

# print(np.array(InfuList).mean())
# pd.DataFrame(np.array(pearX)).to_csv('pearX.csv')
# pd.DataFrame(np.array(pearY)).to_csv('pearY.csv')

keys = sorted(Artists, key=lambda x: Artists[x].influence, reverse=True)
list1 = [['id', 'name', 'genre', 'year', 'influence']]
for i in keys:
    list = []
    list.append(Artists[i].id)
    list.append(Artists[i].name)
    list.append(Artists[i].genre)
    list.append(Artists[i].year)
    list.append(Artists[i].influence)
    list1.append(list)

# pd.DataFrame(list1).to_csv('ArtistsInf.csv', sep=',')


# js = json.dumps(Artists)
# file = open('Artists.txt', 'w')
# file.write(js)
# file.close()
# print("文件输出完成")



pd.DataFrame(list1).to_csv('0.1 SimilarImpact.csv', sep=',')
print("文件输出完成")