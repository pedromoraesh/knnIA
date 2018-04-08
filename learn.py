#!/usr/bin/python
import csv
from sklearn.neighbors import KNeighborsClassifier

if __name__ == '__main__':
    d = csv.reader(open('alturapeso.csv'))
    X = []
    y = []
    for line in d:
        X.append([float(line[0]),float(line[1])])
        y.append(int(line[2]))

neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X, y)
print ("Predição para 1,60 de altura e 50Kg de peso")  
print (neigh.predict([[1.60, 50]]))
print("Predição para 1,89 de altura e 102Kg de peso ")  
print (neigh.predict([[1.89, 102]]))