import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering


df = pd.read_csv(".\sample-embededdings.csv")
#df = pd.read_csv("..\..\embeddings\embeddings.csv")
emData = df['embeddings'].head(100).tolist()
cleanedData = []
# print(emData[29:])
for em in emData:
    emList = em.split(",")
    emDoubleList = []
    for emListItem in emList:
        emDoubleList.append(float(emListItem))
    cleanedData.append(emDoubleList)

hierarchical_cluster = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
labels = hierarchical_cluster.fit_predict(cleanedData)
print("Label data for hierarchial clustering: ")
print(labels)

linkage_data = linkage(cleanedData, method='ward', metric='euclidean')
dendrogram(linkage_data)
plt.show()