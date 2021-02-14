import pandas as pd
import numpy as np

a = np.array([[1, 1, 1], [2, 2, 2]])

df = pd.DataFrame([[1, 1, 1], [2, 2, 2]])

# print(pd.DataFrame.append(df.iloc[0]))
# print(df.iloc[0])
c = np.array([1, 1, 1])

b = np.array([])

list = []
list.append(c)
list.append(c)

array = np.array([[1, 1, 1], [2, 2, 2]])

print(array)
print(array.T)

# data = scale(df.values) # 标准化，标准化之后就自动根据协方差矩阵进行主成分分析了
# pca = PCA(n_components = 1) # 可以调整主成分个数，n_components = 1
# pca.fit(data)
# PCA(copy=True, n_components=1, whiten=False)
# count = 0
# for i in pca.explained_variance_ratio_:
#     count += i
# print(count)
# print("特征根：",pca.explained_variance_) # 输出特征根
# print("解释方差比：",pca.explained_variance_ratio_) # 输出解释方差比
# print("主成分：",pca.components_) # 输出主成分
# print(pca.fit_transform)
# dataframeOut = pd.DataFrame({'特征根':pca.explained_variance_,'解释方差比':pca.explained_variance_ratio_},"主成分：",pca.components_)
# dataframeOut.to_csv("tzg.csv",sep=',', encoding='UTF-8')


# max = 0
# for i in Artists:
#     for j in Artists:
#         if i!=j:
#             # cos = FixCosSimilarity(Artists[i],Artists[j])
#             d = np.linalg.norm(np.array(Artists[i]) - np.array(Artists[j]), ord=2)
#             print(i, j, "欧氏距离", d)


# visited = {}
# stack = []
# def DFS(artist):
#     visited[artist.id] = 1
#     stack.append(artist.id)
#     for sub in artist.impact:
#         if sub not in stack:
#             if sub not in visited:
#                 DFS(Artists[sub])
#         else:
#             index = stack.index(sub)
#             print("有回路"),
#             for i in stack[index:]:
#                 print(i),
#             print(sub)
#     stack.pop(-1)

# for a in Artists:
#     DFS(Artists[a])
#     for a in Artists:
#         viewed[a] = 0
