import random

# define table
table = ["-" for i in range(9)]
can_place = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def game_table():
	print("|", table[0], "|", table[1], "|", table[2], "|")
	print("-------------")
	print("|", table[3], "|", table[4], "|", table[5], "|")
	print("-------------")
	print("|", table[6], "|", table[7], "|", table[8], "|")
	print("----------------------")


def checkWin():
	# rows
	if table[0] == table[1] == table[2]:
		return True
	elif table[3] == table[4] == table[5]:
		return True
	elif table[6] == table[7] == table[8]:
		return True
	# columns
	elif table[0] == table[3] == table[6]:
		return True
	elif table[1] == table[4] == table[7]:
		return True
	elif table[2] == table[5] == table[8]:
		return True
	# diagonal
	elif table[0] == table[4] == table[8]:return True
	elif table[2] == table[4] == table[6]:
		return True
	else:
		return False


def singleplayer():
	global can_place, table, turn

	choice = ["X", "O"]
	p1 = input("X or O?: ").capitalize()

	while p1 not in choice:  
		print("Not \"X\" or \"O\"")
		print("-"*10)
		p1 = input("X or O?: ").capitalize()  # define p1

	if p1 == "O":
		bot = "X"
	else:
		bot = "O"
	
	turn_list = [p1, bot] 
	turn = random.choice(turn_list)

	while True:
		game_table()
		if turn == p1:
			while True:
				try:
					move = int(input("Choose your move![1-9]: ")) - 1  # p1 choose move

					while not move in can_place:
						print("You can't place there!")
						print("----------------------")
						game_table()
						move = int(input("Choose your move![1-9]: ")) - 1
					table[move] = p1  # place player
					can_place.pop(can_place.index(move))  # eliminate choice
					break

				except ValueError:
					print("Number[1-9] please!")
					game_table()
				game_table()
		else:
			bot_move = random.choice(can_place)  # bot choose move
			table[bot_move] = bot  # place bot
			can_place.pop(can_place.index(bot_move))  # eliminate choice
		count = 0
		for i in table:
			if i == turn:
				count += 1
		if count >= 3 and checkWin():
			winner = turn
			break
		if turn == bot:
			turn = p1
		else:
			turn = bot

	game_table()

	if winner == bot:
		print(f"Bot win! [{winner}]")
	else:
		print(f"You win![{winner}]")


def multiplayer():
	pass


def game():
	# start game!
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


game()