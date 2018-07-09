print("Player One, what is your username? Press enter if you want the default username.".center(columns))
		name1 = input("> ")
		if name1.translate(removepunct).translate(removespace) == "":
			name1 = "P1"
		else:
			name1 = name1
		print("Player Two, what is your username? Press enter if you want the default username.".center(columns))
		name2 = input("> ")
		if name2.translate(removepunct).translate(removespace) == "":
			name2 = "P2"
		else:
			name2 = name2