# -*- coding: utf-8 -*-
"""
Assignment: Python for Machine Learning
Using the breast cancer data set demonstrate k-means clustering using the scikit learn package (50 points).

Calculate the sum of least square error for each different values of 'k'. 

Using Matplotlib determine the optimal number of clusters (k) using the elbow method along with an explanation (50 points) .

Finally plot the optimal clusters with their centroids along with a brief explanation (50 points). 
Comment your code as needed.

Datasets used 
Breast Cancer : Link = https://archive.ics.uci.edu/dataset/14/breast+cancer

@author: mitch
"""
from ucimlrepo import fetch_ucirepo
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import pandas as pd
import numpy as np
 
 
#load in the  data set 
# fetch dataset 
breast_cancer = fetch_ucirepo(id=14) 
  
# data (as pandas dataframes) 
X = breast_cancer.data.features 
y = breast_cancer.data.targets 
  
# metadata 
print(breast_cancer.metadata) 
  
# variable information 
print(breast_cancer.variables)

# Fetch the breast cancer dataset
breast_cancer = fetch_ucirepo(id=14)

# Preprocess the data
categorical_columns = ['age', 'menopause', 'tumor-size', 'inv-nodes', 'node-caps', 'deg-malig', 'breast', 'breast-quad', 'irradiat']
numeric_columns = X.select_dtypes(include=['int64', 'float64']).columns

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_columns),
        ('cat', OneHotEncoder(drop='first', sparse=False), categorical_columns)
    ])

X_preprocessed = preprocessor.fit_transform(X)

# Perform k-means clustering for different k values
inertias = []
k_values = range(1, 11)

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_preprocessed)
    inertias.append(kmeans.inertia_)

# Plot the elbow curve
plt.figure(figsize=(10, 6))
plt.plot(k_values, inertias, 'bx-')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal k')
plt.show()

# Determine the optimal number of clusters
optimal_k = 3  # Based on the elbow curve

# Perform k-means clustering with the optimal k
kmeans_optimal = KMeans(n_clusters=optimal_k, random_state=42)
cluster_labels = kmeans_optimal.fit_predict(X_preprocessed)

# Visualize the optimal clusters
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_preprocessed)

plt.figure(figsize=(10, 6))
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=cluster_labels, cmap='viridis')
centers = pca.transform(kmeans_optimal.cluster_centers_)
plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='x', s=100, linewidths=3)
plt.colorbar(scatter)
plt.title(f'K-means Clustering (k={optimal_k})')
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.show()

"""
Explanation of the optimal number of clusters:
The elbow method plot shows the inertia (sum of squared distances of samples to their closest cluster center) 
for different values of k. The optimal number of clusters is typically at the "elbow" of the curve, 
where adding more clusters doesn't significantly reduce the inertia. In this case, the optimal k is 3, 
as the curve begins to level off after this point.

Explanation of the optimal clusters plot:
The scatter plot shows the data points projected onto the first two principal components,
with each point colored according to its assigned cluster. The red X markers represent the cluster centroids.
This visualization helps show how the data is grouped in the reduced dimensional space.
The three clusters likely correspond to different patterns in the breast cancer data,
potentially separating benign and malignant cases, or identifying subgroups within these categories. 
Further analysis of the cluster characteristics would be needed to interpret their clinical significance

"""
