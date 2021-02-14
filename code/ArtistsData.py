import csv
import codecs

from pandas import DataFrame
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from sklearn.metrics.pairwise import cosine_similarity
from sklearn import preprocessing
import datetime
starttime = datetime.datetime.now()


# class Artist:
#     def __init__(self, id, name, danceability, energy, valence, tempo, loudness, mode, key, acousticness,
#                  instrumentalness, liveness, speechiness, duration_ms, popularity, count):
#         self.id = id
#         self.danceability = danceability
#         self.energy = energy
#         self.valence = valence
#         self.tempo = tempo
#         self.loudness = loudness
#         self.mode = mode
#         self.key = key
#         self.acousticness = acousticness
#         self.instrumentalness = instrumentalness
#         self.liveness = liveness
#         self.speechiness = speechiness
#         self.duration_ms = duration_ms
#         self.popularity = popularity
#         self.count = count


# csvFile = open("data_by_artist.csv", "r", encoding='UTF-8')
# reader = csv.reader(csvFile)
# reader = pd.read_csv('data_by_artist.csv', encoding='UTF-8')
# print(reader.shape)

# InfluenceList = [row for row in reader]
# InfluenceList.remove(InfluenceList[0])


df = pd.read_csv("data_by_artist.csv")
ArtistsNum = df.shape[0]
dimension = 13

# #构造艺术家字典
# ArtistsMap = {}
# for index, row in df.iterrows():
#     ArtistsMap[index] = row['artist_id']


df_drop = df.drop(columns=['artist_name', 'count'])
df_drop.set_index(["artist_id"], inplace=True)
df_scale = (df_drop-df_drop.mean())/df_drop.std() #标准化


def FixCosSimilarity(p1, p2):
    mean1 = np.mean(p1)
    mean2 = np.mean(p2)
    fixed1 = [p1[x]-mean1 for x in range(dimension)]
    fixed2 = [p2[x]-mean2 for x in range(dimension)]
    return cosine_similarity([fixed1], [fixed2])[0][0]


counter = 0
RelevanceMat = np.zeros(shape=(ArtistsNum, ArtistsNum))
datalist = df_scale.values
minSim = 0
maxSim = 0
for i in range(ArtistsNum):
    for j in range(i+1, ArtistsNum):
        temp = FixCosSimilarity(datalist[i], datalist[j])
        RelevanceMat[i][j] = temp
        if temp > maxSim:
            maxSim = temp
        if temp < minSim:
            minSim = temp

RelevanceFrame = pd.DataFrame(RelevanceMat)
RelevanceFrame = (RelevanceFrame-minSim)/(maxSim-minSim)


# RelevanceFrame.to_csv("Similarity.csv", sep=',')
# NewArray = RelevanceFrame.values
# np.savetxt('SimilarityArray.csv', NewArray, delimiter=',')
# print("保存文件成功，处理结束")

# array = np.array([[66,14],[35,66]])
# print (array)
# frame = pd.DataFrame(array)
# sss = 5
# frame = (frame+5)/10
# print(frame)
# np.savetxt('Similarity.csv', frame ,delimiter=',')
# print(np.loadtxt('a.csv', delimiter=','))


endtime = datetime.datetime.now()
print ("运行时间", endtime - starttime)