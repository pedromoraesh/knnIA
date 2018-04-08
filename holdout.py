#!/usr/bin/python
import csv
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.grid_search import RandomizedSearchCV
import numpy as np

if __name__ == '__main__':
    d = csv.reader(open('alturapeso.csv'))
    X = []
    y = []
    for line in d:
        X.append([float(line[0]),float(line[1])])
        y.append(int(line[2]))

#Treinando
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)
# print ("Predição para 1,60 de altura e 50Kg de peso")  
# print (neigh.predict([[1.60, 50]]))
# print("Predição para 1,89 de altura e 102Kg de peso ")  
# print (neigh.predict([[1.89, 102]]))


#Test com tamanho de 25%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

k_range = list(range(1, 75))
weight_options = ['uniform', 'distance']
param_dist = dict(n_neighbors=k_range, weights=weight_options)

rscv = RandomizedSearchCV(knn, param_dist, cv=10, scoring='accuracy', n_iter=10, random_state=42)
rscv.fit(X_train, y_train)

print("Best parameters set found:",rscv.best_params_)