import random

# define table
table = ["-" for i in range(9)]
can_place = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def game_table():
	print("-------------")
	print("|", table[0], "|", table[1], "|", table[2], "|")
	print("-------------")
	print("|", table[3], "|", table[4], "|", table[5], "|")
	print("-------------")
	print("|", table[6], "|", table[7], "|", table[8], "|")
	print("-------------")


def checkWin():
	# rows
	if table[0] == table[1] == table[2] != "-":
		return True
	elif table[3] == table[4] == table[5] != "-":
		return True
	elif table[6] == table[7] == table[8] != "-":
		return True
	# columns
	elif table[0] == table[3] == table[6] != "-":
		return True
	elif table[1] == table[4] == table[7] != "-":
		return True
	elif table[2] == table[5] == table[8] != "-":
		return True
	# diagonal
	elif table[0] == table[4] == table[8] != "-":
		return True
	elif table[2] == table[4] == table[6] != "-":
		return True
	else:
		return False


def singleplayer():

	count = 0
	choice = ["X", "O"]
	p1 = input("X or O? >> ").capitalize()

	while p1 not in choice:
		print("Not \"X\" or \"O\"")
		print("-"*10)
		p1 = input("X or O? >> ").capitalize()  # define p1

	if p1 == "O":
		bot = "X"
	else:
		bot = "O"

	turn_list = [p1, bot]
	turn = random.choice(turn_list)

	while True:
		if turn == p1:
			while True:
				try:
					game_table()
					move = int(input(f"Choose your move![1-9] ({turn}) >> ")) - 1  # p1 choose move
					if table[move] == "-":  # place p1
						table[move] = p1
					else:
						print("You can't place there!")
						continue
					can_place.pop(can_place.index(move))  # eliminate choice
					count += 1
					break
				except ValueError:
					print("Number[1-9] please!")
		else:
			bot_move = random.choice(can_place)  # bot choose move
			table[bot_move] = bot  # place bot

			can_place.pop(can_place.index(bot_move))  # eliminate choice
			count += 1
		# print(count)
		if count >= 5 and checkWin():
			winner = turn
			break
		elif count == 9:
			winner = "draw"
			break
		if turn == bot:
			turn = p1
		else:
			turn = bot
	game_table()

	if winner == bot:
		print(f"Bot win! [{winner}]")
	elif winner == p1:
		print(f"You win![{winner}]")
	else:
		print("Draw!")


def multiplayer():
	choice = ["X", "O"]
	count = 0
	p1 = input("p1: X or O? >> ").capitalize()
	while p1 not in choice:
		print("Not \"X\" or \"O\"")
		print("-"*10)
		p1 = input("p1: X or O? >> ").capitalize()

	if p1 == "O":
		p2 = "X"
	else:
		p2 = "O"

	turn_list = [p1, p2]
	turn = random.choice(turn_list)

	while True:
		if turn == p1:
			while True:
				try:
					game_table()
					move = int(input(f"p1 choose your move![1-9] ({turn}) >> ")) - 1  # p1 choose move
					if table[move] == "-":
						table[move] = p1  # place p1
					else:
						print("You can't place there!")
						continue
					can_place.pop(can_place.index(move))  # eliminate choice
					count += 1
					break

				except ValueError:
					print("Number[1-9] please!")
		else:
			while True:
				try:
					game_table()
					move = int(input(f"p2 choose your move![1-9] ({turn}) >> ")) - 1  # p2 choose move
					if table[move] == "-":
						table[move] = p2
					else:
						print("You can't place there!")
						continue
					can_place.pop(can_place.index(move))  # eliminate choice
					count += 1
					break

				except ValueError:
					print("Number[1-9] please!")
		if count >= 5 and checkWin():
			winner = turn
			break
		elif count == 9:
			winner = "draw"
			break

		if turn == p2:
			turn = p1
		else:
			turn = p2

	game_table()

	if winner == p1:
		print(f"p1 win! [{winner}]")
	elif winner == p2:
		print(f"p2 win![{winner}]")
	else:
		print("Draw!")

def again(p):
	if p == 'y':
		return True
	else:
		return False


def game():
	global table, can_place
	user = 'y'
	while again(user):
		# start game!
		table = ["-" for i in range(9)]
		can_place = [0, 1, 2, 3, 4, 5, 6, 7, 8]
		print("Welcome to X-O game!")
		print("----------------------")
		print("Ingame - Label |")
		print("----------------")
		print("|", "1", "|", "2", "|", "3", "|")
		print("-------------")
		print("|", "4", "|", "5", "|", "6", "|")
		print("-------------")
		print("|", "7", "|", "8", "|", "9", "|")
		print("----------------------")
		pick_list = ["1", "2"]
		pick = input("1 or 2 player?: ")

		while pick not in pick_list:
			print("*"*20)
			print("Please input 1 or 2!")
			print("*"*20)
			pick = input("1 or 2 player?: ")
		if pick == "1":
			singleplayer()

		else:
			multiplayer()

		decision = ["y", "n"]
		user = input("Play again? [y/n]: ").lower()
		while user not in decision:
			print("Yes[y] or No[n]")
			user = input("Play again? [y/n]: ").lower()

		again(user)

game()
print("----Game Ended----")
