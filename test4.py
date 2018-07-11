def build():
	if p1mins.mins >= building.cost:
		print("Where would you like to place your building?".center(columns))
		inputted = input("> ").translate(removespace).translate(removepunct).lower()
		#builds 
		if ("{}".format((gameboard[letd[inputted[2]]])[numd[inputted[0:2]]])) == " ":
			if ("{}".format(((gameboard[letd[rletd[letd[inputted[2]]+1]]])))) == " ":
				if ("{}".format((gameboard[letd[inputted[2]]])[numd[inputted[0:2]]+1])) == " ":
					if ("{}".format((gameboard[letd[inputted[2]]])[numd[inputted[0:2]]+1])) == " ":
						if ("{}".format((gameboard[letd[inputted[2]]])[numd[inputted[0:2]]+2])) == " ":
							if ("{}".format(((gameboard[letd[rletd[letd[inputted[2]]+1]]])[numd[inputted[0:2]]+2]))) == " ":
								if ("{}".format((gameboard[letd[inputted[2]]])[numd[inputted[0:2]]])).isalpha() != True:
									if ("{}".format(((gameboard[letd[rletd[letd[inputted[2]]+1]]])[numd[inputted[0:2]]]))).isalpha() != True:
										if ("{}".format((gameboard[letd[inputted[2]]])[numd[inputted[0:2]]+1])).isalpha() != True:
											if ("{}".format(((gameboard[letd[rletd[letd[inputted[2]]+1]]])[numd[inputted[0:2]]+1]))).isalpha() != True:
												if ("{}".format((gameboard[letd[inputted[2]]])[numd[inputted[0:2]]+2])).isalpha() != True:
													if ("{}".format(((gameboard[letd[rletd[letd[inputted[2]]+1]]])[numd[inputted[0:2]]+2]))).isalpha() != True:
														(gameboard[letd[inputted[2]]])[numd[inputted[0:2]]] = "b"
														((gameboard[letd[rletd[letd[inputted[2]]+1]]])[numd[inputted[0:2]]]) = "b"
														(gameboard[letd[inputted[2]]])[numd[inputted[0:2]]+1] = "b"
														((gameboard[letd[rletd[letd[inputted[2]]+1]]])[numd[inputted[0:2]]+1]) = "b"
														(gameboard[letd[inputted[2]]])[numd[inputted[0:2]]+2] = "b"
														((gameboard[letd[rletd[letd[inputted[2]]+1]]])[numd[inputted[0:2]]+2]) = "b"
													else:
														print("You can't put that there!")
												else:
													print("You can't put that there!")
											else:
												print("You can't put that there!")
										else:
											print("You can't put that there!")
									else:
										print("You can't put that there!")
								else:
									print("You can't put that there!")
							else:
								print("You can't put that there!")
						else:
							print("You can't put that there!")
					else:
						print("You can't put that there!")				
				else:
					print("You can't put that there!")			
			else:
				print("You can't put that there!")
		else:
			print("You can't put that there!")