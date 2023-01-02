from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn.model_selection import train_test_split

iris=load_iris()
print("\n IRIS DATA :\n",iris.data)

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=0)

print("\n Target :\n",iris.target)
print("\n X TRAIN \n", X_train)
print("\n X TEST \n", X_test)
print("\n Y TRAIN \n", y_train)
print("\n Y TEST \n", y_test)

kn = KNeighborsClassifier(n_neighbors=5)
kn.fit(X_train, y_train)

for i in range(len(X_test)):
  x_new = np.array([X_test[i]])
  prediction = kn.predict(x_new)
  print("\n Actual : {0} {1}, Predicted :{2}{3}".format(y_test[i],iris["target_names"][y_test[i]],prediction,iris["target_names"][ prediction]))
print("\n TEST SCORE[ACCURACY]: {:.2f}\n".format(kn.score(X_test, y_test)))
