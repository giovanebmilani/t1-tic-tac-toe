from typing import List


class Knn:
	K = 3

	@staticmethod
	def manhattan_distance(data: List[int], sample: List[int]):
		num = 0
		for i in range(len(data)):
			num += abs(data[i] - sample[i])
		return num

	@staticmethod
	def execute(testing_data: List[List[int]], training_data: List[List[int]]):
		for test_data in testing_data:
			distances: List[tuple] = []
			for train_data in training_data:
				distance = Knn.manhattan_distance(test_data, train_data)
				distances.append((distance, train_data[9]))

			distances = sorted(distances, key=lambda d: d[0])

			current_class = None
			max_count = 0
			for c in range(-1, 2):
				count = 0
				for n in range(Knn.K):
					if distances[n][1] == c:
						count += 1

				if count > max_count:
					current_class = c
					max_count = count

			print(current_class)


