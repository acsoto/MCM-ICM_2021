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




# GraphX = []
# GraphY = []
#
# count = 0
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

# # my_dpi = 40
# # figsize=(480 / my_dpi, 480 / my_dpi), dpi=my_dpi
# plt.figure(figsize=(8,5))
# my_circle = plt.Circle((0, 0), 0.4, color='white')
#
# plt.pie(GraphY, colors=Pastel1_7.hex_colors)
# p = plt.gcf()
# p.gca().add_artist(my_circle)
# plt.legend(loc='best', labels=GraphX, bbox_to_anchor=(1, 1))
# # plt.show()
# plt.savefig("filename.png")