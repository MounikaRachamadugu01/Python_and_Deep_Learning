"""
1.Apply K means clustering in this data set provided below:
https://umkc.box.com/s/a9lzu9qoqfkbhjwk5nz9m6dyybhl1wqy
Remove any null values by the mean.
Use the elbow method to find a good number of clusters with the KMeans algorithm
2.Calculate the silhouette score for the above clustering
3.Try feature scaling to see if it will improve the Silhouette score
4.Apply PCA on the same dataset.

*** Bonuspoints
1.Apply kmeans algorithm on the PCA result and report your observation if the score improved or not?
    a.You can try different variation like PCA+KMEANS , SCALING+PCA+KMEANS.
2.Visualize the clustering of first bonus question
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import seaborn as sns
sns.set(style="white", color_codes=True)
import warnings
warnings.filterwarnings("ignore")

# Loading dataset using pandas library
dataset = pd.read_csv('CC.csv')

# Finding null values count for each feature and displaying them
nulls = pd.DataFrame(dataset.isnull().sum().sort_values(ascending=False))
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
print(nulls)

# Removing null values and replacing with mean
dataset['MINIMUM_PAYMENTS'].fillna(dataset['MINIMUM_PAYMENTS'].mean(), inplace=True)
dataset['CREDIT_LIMIT'].fillna(dataset['CREDIT_LIMIT'].mean(), inplace=True)
replacednulls = pd.DataFrame(dataset.isnull().sum().sort_values(ascending=False))
replacednulls.columns = ['Null Count']
replacednulls.index.name = 'Feature'
print(replacednulls)

x = dataset.iloc[:, 1:-1]

# Using elbow method
wcss = []  # declaring list

for i in range(1, 7):
    kmeans = KMeans(n_clusters=i, max_iter=300, random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 7), wcss)
plt.title('Elbow method')
plt.xlabel('number of clusters')
plt.ylabel('wcss')
plt.show()

# Creating the model
km = KMeans(n_clusters=3)
km.fit(x)

# Predicting the cluster for each data point
y_cluster_kmeans = km.predict(x)

# calculating the score using metrics
score = metrics.silhouette_score(x, y_cluster_kmeans)
print("\n Actual score:", score)

# scaling
scaler = StandardScaler()
# Training
scaler.fit(x)
x_scaler = scaler.transform(x)

# Applying kmeans algorithm
nclusters = 3  # k value in k-means
km = KMeans(n_clusters=3)
km.fit(x_scaler)
y_cluster_kmeansscale = km.predict(x_scaler)

# calculating the score
kmeansscore = metrics.silhouette_score(x_scaler, y_cluster_kmeansscale)
print("Score after scaling:", kmeansscore)

# Applying PCA
pca = PCA(2)
x_pca = pca.fit_transform(x)

# applying pca on scaled data x-scaler
pca = PCA(2)
x_pca_scaler = pca.fit_transform(x_scaler)

# PCA+KMEANS
# Creating the model
km = KMeans(n_clusters=3)
km.fit(x_pca)
# Predicting the cluster for each data point
y_cluster_pcakmeans = km.predict(x_pca)

pcakmeansscore = metrics.silhouette_score(x_pca, y_cluster_pcakmeans)
print("Score after pca+kmeans:", pcakmeansscore)

# SCALING+PCA+KMEANS

# Creating the model
km = KMeans(n_clusters=3)
km.fit(x_pca_scaler)
# predict the cluster for each data point
y_cluster_scalerpcakmeans = km.predict(x_pca_scaler)

scalepcakmeanscore = metrics.silhouette_score(x_pca_scaler, y_cluster_scalerpcakmeans)
print("Score after scaling+pca+kmeans:", scalepcakmeanscore)

# plot for pca+kmeans
plt.scatter(x_pca[:, 0], x_pca[:, 1], c=y_cluster_kmeans, s=50, cmap='viridis')
plt.show()

# plot for SCALING+PCA+KMEANS
plt.scatter(x_pca_scaler[:, 0], x_pca_scaler[:, 1], c=y_cluster_kmeans, s=50, cmap='viridis')
plt.show()


