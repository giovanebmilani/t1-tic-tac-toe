from sklearn.neural_network import MLPClassifier
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

# criando nossa MLP
# activation controla a função de ativação
# tol parametro para controlar a saida das epocas caso a melhora do algoritmo nao seja maior que esse numero
mlp = MLPClassifier(hidden_layer_sizes=(5, 2), activation='relu', solver='lbfgs', max_iter=1000, tol=1e-5)

mlp.fit(training_x, training_y)

# accuracy = mlp.score(testing_x, testing_y)

# print("Number of iterations:", mlp.n_iter_)
# print("Acuracia da MLP: {:.2f}%".format(accuracy * 100))

