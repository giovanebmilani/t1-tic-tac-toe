from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

# dataset para treinamento e teste
training_data = pd.read_csv("src/data/training.data", header=None)
testing_data = pd.read_csv("src/data/testing.data", header=None)

# separando dados das classes
training_x = training_data.iloc[:, :-1]
training_y = training_data.iloc[:, -1]

# separando dados das classes
testing_x = testing_data.iloc[:, :-1]
testing_y = testing_data.iloc[:, -1]

# criando o Knn
k = 1
knn = KNeighborsClassifier(n_neighbors=k)

knn.fit(training_x, training_y)

accuracy = knn.score(testing_x, testing_y)

print("Acuracia Knn: {:.2f}%".format(accuracy * 100))