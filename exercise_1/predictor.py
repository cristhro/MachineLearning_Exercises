#!/usr/bin/env

import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'
lista=sys.argv
lista.remove(lista[0])


from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

iris = load_iris()
data_frame = pd.DataFrame(   data=np.c_[iris['data'], iris['target']],
                     columns= iris['feature_names'] + ['target'])

# Lo transformamos en un pandas
X = data_frame[iris['feature_names']]  # features
y = data_frame['target']               # targets


# Vamos a entrenar 
from sklearn.neighbors import KNeighborsClassifier

# Modelo
knn = KNeighborsClassifier(n_neighbors=20)
knn.fit(X,y)

# Resultado
print(knn.predict([lista]))

