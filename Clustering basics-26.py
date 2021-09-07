## 2. The Dataset ##

import pandas as pd
votes = pd.read_csv('114_congress.csv')


## 3. Exploring the Data ##

print(votes['party'].value_counts())
print(votes.mean())


## 4. Distance between Senators ##

from sklearn.metrics.pairwise import euclidean_distances

print(euclidean_distances(votes.iloc[0,3:].values.reshape(1, -1), votes.iloc[1,3:].values.reshape(1, -1)))

distance = euclidean_distances(votes.iloc[0,3:].values.reshape(1, -1), votes.iloc[2,3:].values.reshape(1, -1))

## 6. Initial Clustering ##

import pandas as pd
from sklearn.cluster import KMeans

kmeans_model = KMeans(n_clusters=2, random_state=1)
senator_distances = kmeans_model.fit_transform(votes.iloc[:,3:])

## 7. Exploring the Clusters ##

labels = kmeans_model.labels_
print(pd.crosstab(labels, votes['party']))

## 8. Exploring Senators in the Wrong Cluster ##

democratic_outliers = votes[(labels == 1) & (votes['party'] == "D")]
print(democratic_outliers)

## 9. Plotting out the Clusters ##

plt.scatter(x = senator_distances[:,0], y = senator_distances[:,1], c = labels, linewidths = 0)
plt.show()

## 10. Finding the Most Extreme ##

extremism = (senator_distances**3).sum(axis = 1)
votes['extremism'] = extremism
votes.sort_values('extremism', inplace = True, ascending = False)
print(votes.head(10))