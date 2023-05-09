from sklearn.tree import DecisionTreeClassifier
import pandas as pd

# dataset para treinamento e teste
training_data = pd.read_csv("src/data/trainingCerto.data", header=None)
testing_data = pd.read_csv("src/data/testingCerto.data", header=None)

# separando dados das classes
training_x = training_data.iloc[:, :-1]
training_y = training_data.iloc[:, -1]

# separando dados das classes
testing_x = testing_data.iloc[:, :-1]
testing_y = testing_data.iloc[:, -1]

decision_tree = DecisionTreeClassifier()

decision_tree.fit(training_x, training_y)

accuracy = decision_tree.score(testing_x, testing_y)

print("Acuracia da Arvore de decisao: {:.2f}%".format(accuracy * 100))