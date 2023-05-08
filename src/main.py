import os
from constants import algorithms


class TicTacToe:
    
	def __init__(self, algorithms: list):
		self.algorithms = algorithms
		self.current_algo = None
		self.tictactoe = None
		self.turn = 'X'

	def start_game(self):
		self.tictactoe = [
			0, 0, 0,
			0, 0, 0,
			0, 0, 0
		]
	
	def round(self):
		print(f'\n{self.turn} is playing.')
		playing = None
		if self.turn == 'X':
			playing = 1
			self.turn = 'O'
		elif self.turn == 'O':
			playing = -1
			self.turn = 'X'

		play = input("Insert position to play: ")

		self.tictactoe[int(play)-1] = playing
	
	def get_string_by_index(self, index: int):
		if self.tictactoe[index] == 1:
			return 'X'
		elif self.tictactoe[index] == -1:
			return 'O'
		return index + 1

	def print_game(self):
		g = self.tictactoe
		for i in range(0, 9, 3):
			print(f' {self.get_string_by_index(i)} | {self.get_string_by_index(i+1)} | {self.get_string_by_index(i+2)}')
			if i < 6 and i % 3 == 0:
				print('---|---|---')

	def run(self):
		while True:
			print('=== TIC TAC TOE ===')
			for algo in self.algorithms:
				print(f'{algo["id"]}. {algo["name"]}')

			user_input = input("Type the code of the algorithm or 'exit': ")

			if user_input == 'exit':
				break
			
			if user_input.isnumeric():
				user_input = int(user_input)
				self.current_algo = list(filter(lambda a: a['id'] == user_input, self.algorithms))[0]

				os.system('clear')	
				self.start_game()
				while self.current_algo is not None:
					print('\n')
					print(f'Algo is {self.current_algo["name"]}')
					print('\n')
					self.print_game()
					self.round()
					os.system('clear')

if __name__ == '__main__':
	tictactoe = TicTacToe(algorithms=algorithms)
	tictactoe.run()