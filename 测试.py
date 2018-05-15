import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, Normalizer

def importData(filename):
    """ D每年获得的飞行常客里程数
        D玩视频游戏所耗时间百分比
        D每周消费的冰淇淋公升数"""
    filename = 'datingTestSet.txt'
    columns_names = ['flight', 'games', 'icecream', 'type']
    initData = pd.read_csv(filename, delimiter='\t', names = columns_names)
    enc = LabelEncoder()
    enc.fit(initData.type)
    labels = enc.transform(initData.type)
    del initData['type']
    # ,index_col = np.range(1000)
    # plt.plot(initData.iloc[:, 0])
    # plt.show()
    # plt.scatter(initData.flight, initData.icecream)
    # plt.show()
    return initData, labels

if __name__ == '__main__':
    print(importData(123))
    # originalData, targets = importData(123)
    # scaler = Normalizer().fit()
