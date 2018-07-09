import shutil
import re
import string
columns = shutil.get_terminal_size().columns
def intro():
	print("Welcome to CIV: Command Line!".center(columns))
	input("Press enter to begin.".center(columns))
	print("")
def start():
	i = 0
	while i == i:
		print("Input s to start the game, t to run through the tutorial, and q to quit.".center(columns))
		removepunct = str.maketrans('', '', string.punctuation)
		removespace = str.maketrans('', '', string.whitespace)
		ip = input("> ").translate(removepunct).translate(removespace).lower()
		if ip == "s":
			game()
			break
		elif ip == "t":
			tutorial()
			break
		elif ip == "q":
			print("Thanks for playing!".center(columns))
			quit()
		else:
			print("Oops, that's not a valid option! Try again".center(columns))
			print("")
			i += 1
def game():
	removepunct = str.maketrans('', '', string.punctuation)
	removespace = str.maketrans('', '', string.whitespace)
	print("Welcome to the world of CIV:CL!".center(columns))
	if input("Press enter to continue, or if you would like to return to the home screen, input 'q'".center(columns)).translate(removepunct).translate(removespace).lower() == "q":
		start()
	else:
		initplay = ["One","Two"]
		players = []
		print("")
		for player in initplay:
			print("Player {}, what is your username? Press enter if you want the default username.".center(columns).format(player))
			name = input("> ")
			if name.translate(removepunct).translate(removespace) == "":
				players.append("P{}".format(str(initplay.index(player)+1)))
			else:
				players.append(name)
		col = 202
		lin = 52
		l = []
		print(players)
		print("")
		input("Note: At no point are you allowed to look at the other player's board; that is what we call cheating! Press enter to display the first player's board, and begin the game.".center(columns))
		print("")
		for player in players:
			print("Here is {}'s starting board:".format(player).center(columns))
			print(("="*(col-2)).center(columns))
			for i in range(lin-3):
				l.append(("|"+"·"*(col-4)+"|"))
			for i in range(lin-3):
				print(l[i].center(columns))
			print(("="*(col-2)).center(columns))
			input("Press enter to continue.")
			for i in range(lin-21):
				print("")
	start()
def tutorial():
	print("Sorry, this feature has not been added yet :(".center(columns))
	print("")
	start()
intro()
start()