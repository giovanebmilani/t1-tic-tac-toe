import os
from constants import algorithms


class TicTacToe:
    
	def __init__(self, algorithms: list):
		self.algorithms = algorithms
		self.current_algo = None
		self.tictactoe = None
		self.turn = 'X'

	def start_game(self):
		self.turn = 'X'
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

		while True:
			play = input("Insert position to play or indicate 'error': ")

			if play == 'error':
				self.current_algo['errors'] += 1

			if play.isnumeric():
				play = int(play)
				if self.tictactoe[play-1] == 0:
					break

		self.tictactoe[play-1] = playing
	
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

	def get_ai_predict(self):
		ai = self.current_algo['algo']
		return ai.predict([self.tictactoe])[0]
	
	def get_formatted_ai_predict(self):
		predict = self.get_ai_predict()
		if predict == 0:
			return 'WIN'
		elif predict == 1:
			return 'DRAW'
		elif predict == 2:
			return 'ONGOING'

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
					iterations = self.current_algo["iterations"]
					errors = self.current_algo["errors"]
					print(f'Algo is {self.current_algo["name"]}')
					if iterations > 0:
						print(f'Iterations: {iterations}')
						print(f'❌ {round(errors/iterations*100, 2)}% | ✅ {round((1-errors/iterations)*100,2)}%')
					print('\n')

					self.print_game()
					print('\n')
					print(f'AI predict: {self.get_formatted_ai_predict()}')

					self.current_algo['iterations'] += 1

					ia_predict = self.get_ai_predict()

					user_input = input('is IA prediction right (y/n)?')

					if user_input == 'n':
						self.current_algo['errors'] += 1
						if ia_predict == 2:
							print('\n\n')
							break

					if ia_predict == 0 or ia_predict == 1:
						if user_input == 'y':
							print('Game Over.\n\n')
							break
					
					self.round()
				
					os.system('clear')
				
if __name__ == '__main__':
	tictactoe = TicTacToe(algorithms=algorithms)
	tictactoe.run()