from knn.main import Knn
from data.processing import read_file_in_lines, process_data

def read_data(filename: str):
	with open(filename, 'r') as file:
		lines = file.readlines()
	formated = []
	for line in lines:
		line = line.split(',')
		new_line = []
		for char in line:
			new_line.append(int(char))
		formated.append(new_line)
	return formated
    

test = read_data('new_data.data')
train = read_data('new_data.data')

Knn.execute(test, train)