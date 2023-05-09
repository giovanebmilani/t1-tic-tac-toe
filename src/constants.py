from mlp.main import mlp
from knn.main import knn
from decision_tree.main import decision_tree

algorithms = [
    {
        'id': 1,
        'name': 'K-Nearest-Neighborns',
        'algo': knn
	},
    {
        'id': 2,
        'name': 'Multiple Layer Perceptron',
        'algo': mlp
	},
    {
        'id': 3,
        'name': 'Decision Tree',
        'algo': decision_tree
	}
]