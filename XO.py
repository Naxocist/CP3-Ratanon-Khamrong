import random

# define table
table = ["-" for i in range(9)]
choice = ["X", "O"]
can_place = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def game_table():
	print("|", table[0], "|", table[1], "|", table[2], "|")
	print("-------------")
	print("|", table[3], "|", table[4], "|", table[5], "|")
	print("-------------")
	print("|", table[6], "|", table[7], "|", table[8], "|")

def checkWin():
	do = ""
	for i in table:
		if i == "-":
			do = "no"
			break
	if do == "no":
		return False
	else:
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
		# diagonals
		elif table[0] == table[4] == table[8]:
			return True
		elif table[2] == table[4] == table[6]:
			return True
		else:
			return False


def botPick():
	pass

def singleplayer():
	p1 = input("You want X or O?: ")
	choice.pop(choice.index(p1))
	bot = choice[0]  # define bot
	while not checkWin():
		game_table()  # display table
		move = int(input("Choose your move![1-9]: ")) - 1  # p1 choose move
		while move not in can_place:
			print("You can't place there!")
			move = int(input("Choose your move![1-9]: ")) - 1
		table[move] = p1  # place player
		can_place.pop(move)  # eliminate choice

		bot_move = random.choice(can_place)  # bot choose move
		table[bot_move] = bot  # place bot
		can_place.pop(bot_move)  # eliminate choice
	print("game end")


def multiplayer():
	pass


# start game!
print("Welcome to X-O game!")
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
