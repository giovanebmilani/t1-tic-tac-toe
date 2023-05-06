from typing import List

win_patterns = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 4, 8],
    [2, 4, 6],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8]
]


WIN = '0'
DRAW = '1'
ONGOING = '2'


def read_file_in_lines(filename: str) -> List[str]:
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines

def process_data(data: List[str]) -> List[str]:
	new_data = []
	for game in data:
		game = game.split(',')
		game[9] = DRAW

		for i in range(8):
			if game[i] == 'b':
				game[9] = ONGOING

		for pattern in win_patterns:
			if game[pattern[0]] != 'b' and game[pattern[0]] == game[pattern[1]] and game[pattern[1]] == game[pattern[2]]:
				game[9] = WIN
		new_data.append(game)
	return new_data

def save_data(data: List[str], filename: str):
	with open(filename, 'w') as file:
		for line in data:
			line = ','.join(line) + '\n'
			line = line.replace('x', '1')
			line = line.replace('b', '0')
			line = line.replace('o', '-1')
			file.write(line)


# data = read_file_in_lines('tic-tac-toe.data')

# new_data = process_data(data)

# save_data(new_data, 'new_data.data')
