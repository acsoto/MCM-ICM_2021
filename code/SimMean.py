import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib import cm
from palettable.colorbrewer.qualitative import Pastel1_7


df = pd.read_csv('ArtistsInf.csv')
df.drop(['Unnamed: 0'], axis=1, inplace=True)
df.drop([0], axis=0, inplace=True)
array = df.values
# 提取到array
#############
SimFrame = pd.read_csv("Similarity.csv")
SimFrame.drop(['Unnamed: 0'], axis=1, inplace=True)
SimArray = SimFrame.values
print("相似度矩阵读取完毕")
#############
ArtistsMap = {}
data_by_artist_array = pd.read_csv("data_by_artist.csv").values
#############


list = []
for i in range(5854):
    for j in range(i+1, 5854):
        list.append(SimArray[i][j])

print(np.mean(list))



