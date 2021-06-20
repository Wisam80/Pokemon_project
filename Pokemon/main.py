import random


class Move:
	def __init__(self, name, health_reduced):
		self.name = name
		self.health_reduced = health_reduced

class Type:
	def __init__(self,name,weakness):
		self.name = name
		self.weakness = weakness



class Pokemon:

	def __init__(self, name, max_health, moves,types):
		self.name = name
		self.max_health = max_health
		self.moves = moves
		self.types = types

		self.current_health = max_health

	def get_attacked(self, amount):
		self.current_health -= amount


	def is_alive(self):
		return self.current_health > 0







class Game:

	def __init__(self):
		# Create all possible Moves
		self.moves = {"tackle": Move("Tackle", 10), "punch": Move("Punch", 20), "pokekick": Move("Kick",30),
					  "mega_punch": Move("Mega_punch",50), "fire_punch": Move("Fire_punch", 40)}



		# Create all possible Pokemon
		self.pokemon = {
			"pikachu": Pokemon("pikachu", 100, [self.moves["tackle"],self.moves["punch"]], Type("electric",["plant"])),
			"charmander": Pokemon("charmander", 120, [self.moves["fire_punch"],self.moves["mega_punch"]], Type("fire",["water"]))
		}

		self.player_1_pokemon = None
		self.player_2_pokemon = None

		# Create all possible Pokemon types
		self.types = [
			Type("water", ["plant", "electric"]),
			Type("fire", ["water"]),
			Type("plant", ["fire"]),
			Type("electric", [])
		]



	def start_game(self):
		# Ask what pokemon each player wants to choose (From the list created above)

		game_type = input("Do you want to play against a computer or a human? ")
		if game_type == "computer":
			self.player2_computer = True
		else:
			self.player2_computer = False

		current_player = input("choose a pokemon:" )

		if current_player in self.pokemon:
			self.player_1_pokemon = self.pokemon[current_player]
		else:
			print("Not a valid pokemon", current_player)

		current_player = input("choose a pokemon:")

		if current_player in self.pokemon:
			self.player_2_pokemon = self.pokemon[current_player]
		else:
			print("Not a valid pokemon", current_player)

	def check_game_is_over(self):
		if self.player_1_pokemon.is_alive() != True:
			if self.player2_computer:
				print("The computer has won! Game is over!")
			else:
				print("Player 2 has won! Game is over!")
			return True
		if self.player_2_pokemon.is_alive() != True:
			print("Player 1 has won! Game is over!")
			return True
		return False

	def take_turn(self, player):
		# Take in a users chosen move (number between 1 & 2)



		current_pokemon, opponent_pokemon = (
			self.player_1_pokemon, self.player_2_pokemon) if player == "player_1" else (
			self.player_2_pokemon, self.player_1_pokemon)

		print(current_pokemon.name)

		if player == "player_2" and self.player2_computer:
			player_move = '1' if random.random() > 0.5 else '2'
		else:
			player_move = input("choose a move: ")


		if player_move == "1" or player_move == "2":
			print(current_pokemon.moves[int(player_move)-1].name)
		else:
			print("invalid option")
			return

		amount=current_pokemon.moves[int(player_move)-1].health_reduced
		opponent_pokemon.get_attacked(amount)
		print(opponent_pokemon.name,opponent_pokemon.current_health)

		# Acknowledge that you've recieved that move (print it back out or something)
		pass

	def run_game(self):

		current_player = 'player_1'
		game_is_over = False

		while not game_is_over:
			# 1. Take the current players turn
			self.take_turn(current_player)

			# 2. Check to see if the game is over after this turn
			game_is_over = self.check_game_is_over()

			# 3. Switch to the other players turn
			if current_player == 'player_1':
				current_player = 'player_2'
			else:
				current_player = 'player_1'

game = Game()
game.start_game()
game.run_game()

