import pandas as pd
import numpy as np

pearX = pd.read_csv('pearX.csv').drop(['Unnamed: 0'], axis=1).values
pearY = pd.read_csv('pearY.csv').drop(['Unnamed: 0'], axis=1).values

# data = pd.DataFrame({'A':np.random.randint(1, 100, 10),
#                      'B':np.random.randint(1, 100, 10),
#                      'C':np.random.randint(1, 100, 10)})


PearsonList = []
for i in range(13):
    listX = []
    listY = []
    for j in range(len(pearX)):
        listX.append(pearX[j][i])
        listY.append(pearY[j][i])
    array = np.array((np.array(listX), np.array(listY)))
    df = pd.DataFrame(array.T)
    PearsonList.append(df.corr()[0][1])

# pd.DataFrame(np.array(PearsonList)).to_csv('pearson.csv')