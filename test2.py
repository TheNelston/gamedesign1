import shutil
import string
class p1mins(object):
	mins = 200
class p2mins(object):
	mins = 200
removepunct = str.maketrans('', '', string.punctuation)
removespace = str.maketrans('', '', string.whitespace)
columns = shutil.get_terminal_size().columns
gameboard = [["="*103],['a', '|', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '|'], ['b', '|', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '|'], ['c', '|', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '|'], ['d', '|', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '|'], ['e', '|', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '|'], ['f', '|', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '|'], ['g', '|', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '|'], ['h', '|', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '|'], ['i', '|', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '|'], ['j', '|', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '|'], ['k', '|', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '|'], ['l', '|', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '|'], ['m', '|', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '|'], ['n', '|', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '|'], ['o', '|', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '|'], ['p', '|', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '|'], ['q', '|', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '|'], ['r', '|', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '|'], ['s', '|', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '|'], ['t', '|', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '|'], ['u', '|', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '|'], ['v', '|', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '|'], ['w', '|', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '|'], ['x', '|', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '|'], ['y', '|', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '|'],["="*103],[" 0000000000111111111122222222223333333333444444444455555555556666666666777777777788888888889999999999"],[" 0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789"]]
for element in gameboard:
	print(("".join(element)).center(columns))
letcoords = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']
letnum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
numcoords = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99']
numnum = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101]
w = -100
letd = dict(zip(letcoords,letnum))
numd = dict(zip(numcoords,numnum))
rletd = dict(zip(letnum,letcoords))
rnumd = dict(zip(numnum,numcoords))
class building(object):
	health = 1000
	mark = "B"
	cost = 100
class unit(object):
	health = 50
	mark = "x"
	cost = 25
def attack():
	print("Where would you like to attack?".center(columns))
	inputted = input("> ").translate(removespace).translate(removepunct).lower()
	if (gameboard[letd[inputted[2]]])[numd[inputted[0:2]]] == building.mark:
		building.health -= 10
		print("This building now has {} hp".format(building.health))
	else:
		print("That's not a building!".center(columns))
def unit():
	if p1mins.minerals >= unit.cost:
		print("Where would you like to place your unit?".center(columns))
		inputted = input("> ").translate(removespace).translate(removepunct).lower()
		if (gameboard[letd[inputted[2]]])[numd[inputted[0:2]]].isalpha() == True:
			print("You can't place that there!".center(columns))
		else:
			(gameboard[letd[inputted[2]]])[numd[inputted[0:2]]] = unit.mark
			for i in range (1,2):	
				if ((gameboard[letd[rletd[letd[inputted[2]]+i]]])[numd[inputted[0:2]]]).isalpha() != True:
					((gameboard[letd[rletd[letd[inputted[2]]+i]]])[numd[inputted[0:2]]]) = " "
				if ((gameboard[letd[rletd[letd[inputted[2]]-i]]])[numd[inputted[0:2]]]).isalpha() != True:
					((gameboard[letd[rletd[letd[inputted[2]]-i]]])[numd[inputted[0:2]]]) = " "
			for i in range(1,3):
				if (gameboard[letd[inputted[2]]])[numd[inputted[0:2]]+i].isalpha() != True:
					(gameboard[letd[inputted[2]]])[numd[inputted[0:2]]+i] = " "
				if (gameboard[letd[inputted[2]]])[numd[inputted[0:2]]-i].isalpha() != True:
					(gameboard[letd[inputted[2]]])[numd[inputted[0:2]]-i] = " "
				if ((gameboard[letd[rletd[letd[inputted[2]]+1]]])[numd[inputted[0:2]]+i]).isalpha() != True:
					((gameboard[letd[rletd[letd[inputted[2]]+1]]])[numd[inputted[0:2]]+i]) = " "
				if ((gameboard[letd[rletd[letd[inputted[2]]-1]]])[numd[inputted[0:2]]+i]).isalpha() != True:
					((gameboard[letd[rletd[letd[inputted[2]]-1]]])[numd[inputted[0:2]]+i]) = " "
				if ((gameboard[letd[rletd[letd[inputted[2]]+1]]])[numd[inputted[0:2]]-i]).isalpha() != True:
					((gameboard[letd[rletd[letd[inputted[2]]+1]]])[numd[inputted[0:2]]-i]) = " "
				if ((gameboard[letd[rletd[letd[inputted[2]]-1]]])[numd[inputted[0:2]]-i]).isalpha() != True:
					((gameboard[letd[rletd[letd[inputted[2]]-1]]])[numd[inputted[0:2]]-i]) = " "
		p1mins.mins -= unit.cost
		for element in gameboard:
			print(("".join(element)).center(columns))
	else:
		print("You don't have enough minerals for that!".center(columns))
def build():
	if p1mins.mins >= building.cost:
		print("Where would you like to place your building?".center(columns))
		inputted = input("> ").translate(removespace).translate(removepunct).lower()
		#builds 
		if ("{}".format((gameboard[letd[inputted[2]]])[numd[inputted[0:2]]])).isalpha() != True:
			if ("{}".format(((gameboard[letd[rletd[letd[inputted[2]]+1]]])[numd[inputted[0:2]]]))).isalpha() != True:
				if ("{}".format((gameboard[letd[inputted[2]]])[numd[inputted[0:2]]+1])).isalpha() != True:
					if ("{}".format(((gameboard[letd[rletd[letd[inputted[2]]+1]]])[numd[inputted[0:2]]+1]))).isalpha() != True:
						if ("{}".format((gameboard[letd[inputted[2]]])[numd[inputted[0:2]]+2])).isalpha() != True:
							if ("{}".format(((gameboard[letd[rletd[letd[inputted[2]]+1]]])[numd[inputted[0:2]]+2]))).isalpha() != True:
								(gameboard[letd[inputted[2]]])[numd[inputted[0:2]]] = building.mark
								((gameboard[letd[rletd[letd[inputted[2]]+1]]])[numd[inputted[0:2]]]) = "b"
								(gameboard[letd[inputted[2]]])[numd[inputted[0:2]]+1] = "b"
								((gameboard[letd[rletd[letd[inputted[2]]+1]]])[numd[inputted[0:2]]+1]) = "b"
								(gameboard[letd[inputted[2]]])[numd[inputted[0:2]]+2] = "b"
								((gameboard[letd[rletd[letd[inputted[2]]+1]]])[numd[inputted[0:2]]+2]) = "b"
							else:
								print("You can't put that there!".center(columns))
						else:
							print("You can't put that there!".center(columns))		
					else:
						print("You can't put that there!".center(columns))
				else:
					print("You can't put that there!".center(columns))
			else:
				print("You can't put that there!".center(columns))
		else:
			print("You can't put that there!".center(columns))
		#removes fog of war
		if ("{}".format((gameboard[letd[inputted[2]]])[numd[inputted[0:2]]+3])).isalpha() != True:
			(gameboard[letd[inputted[2]]])[numd[inputted[0:2]]+3] = " "
		if ("{}".format(((gameboard[letd[rletd[letd[inputted[2]]+1]]])[numd[inputted[0:2]]+3]))).isalpha() != True:
			((gameboard[letd[rletd[letd[inputted[2]]+1]]])[numd[inputted[0:2]]+3]) = " "
		if ("{}".format((gameboard[letd[inputted[2]]])[numd[inputted[0:2]]+4])).isalpha() != True:
			(gameboard[letd[inputted[2]]])[numd[inputted[0:2]]+4] = " "
		if ("{}".format(((gameboard[letd[rletd[letd[inputted[2]]+1]]])[numd[inputted[0:2]]+4]))).isalpha() != True:
			((gameboard[letd[rletd[letd[inputted[2]]+1]]])[numd[inputted[0:2]]+4]) = " "
		if ("{}".format((gameboard[letd[inputted[2]]])[numd[inputted[0:2]]+5])).isalpha() != True:
			(gameboard[letd[inputted[2]]])[numd[inputted[0:2]]+5] = " "
		if ("{}".format(((gameboard[letd[rletd[letd[inputted[2]]+1]]])[numd[inputted[0:2]]+5]))).isalpha() != True:
			((gameboard[letd[rletd[letd[inputted[2]]+1]]])[numd[inputted[0:2]]+5]) = " "
		if ("{}".format((gameboard[letd[inputted[2]]])[numd[inputted[0:2]]-1])).isalpha() != True:
			(gameboard[letd[inputted[2]]])[numd[inputted[0:2]]-1] = " "
		if ("{}".format(((gameboard[letd[rletd[letd[inputted[2]]+1]]])[numd[inputted[0:2]]-1]))).isalpha() != True:
			((gameboard[letd[rletd[letd[inputted[2]]+1]]])[numd[inputted[0:2]]-1]) = " "
		if ("{}".format((gameboard[letd[inputted[2]]])[numd[inputted[0:2]]-2])).isalpha() != True:
			(gameboard[letd[inputted[2]]])[numd[inputted[0:2]]-2] = " "
		if ("{}".format(((gameboard[letd[rletd[letd[inputted[2]]+1]]])[numd[inputted[0:2]]-2]))).isalpha() != True:
			((gameboard[letd[rletd[letd[inputted[2]]+1]]])[numd[inputted[0:2]]-2]) = " "
		if ("{}".format((gameboard[letd[inputted[2]]])[numd[inputted[0:2]]-3])).isalpha() != True:
			(gameboard[letd[inputted[2]]])[numd[inputted[0:2]]-3] = " "
		if ("{}".format(((gameboard[letd[rletd[letd[inputted[2]]+1]]])[numd[inputted[0:2]]-3]))).isalpha() != True:
			((gameboard[letd[rletd[letd[inputted[2]]+1]]])[numd[inputted[0:2]]-3]) = " "
		for i in range (2,3):
			if ("{}".format(((gameboard[letd[rletd[letd[inputted[2]]+i]]])[numd[inputted[0:2]]]))).isalpha() != True:
				((gameboard[letd[rletd[letd[inputted[2]]+i]]])[numd[inputted[0:2]]]) = " "
			if ("{}".format(((gameboard[letd[rletd[letd[inputted[2]]+i]]])[numd[inputted[0:2]]+1]))).isalpha() != True:
				((gameboard[letd[rletd[letd[inputted[2]]+i]]])[numd[inputted[0:2]]+1]) = " "
			if ("{}".format(((gameboard[letd[rletd[letd[inputted[2]]+i]]])[numd[inputted[0:2]]+2]))).isalpha() != True:
				((gameboard[letd[rletd[letd[inputted[2]]+i]]])[numd[inputted[0:2]]+2]) = " "
			if ("{}".format(((gameboard[letd[rletd[letd[inputted[2]]+i]]])[numd[inputted[0:2]]+3]))).isalpha() != True:
				((gameboard[letd[rletd[letd[inputted[2]]+i]]])[numd[inputted[0:2]]+3]) = " "
			if ("{}".format(((gameboard[letd[rletd[letd[inputted[2]]+i]]])[numd[inputted[0:2]]+4]))).isalpha() != True:
				((gameboard[letd[rletd[letd[inputted[2]]+i]]])[numd[inputted[0:2]]+4]) = " "
			if ("{}".format(((gameboard[letd[rletd[letd[inputted[2]]+i]]])[numd[inputted[0:2]]+5]))).isalpha() != True:
				((gameboard[letd[rletd[letd[inputted[2]]+i]]])[numd[inputted[0:2]]+5]) = " "
			if ("{}".format(((gameboard[letd[rletd[letd[inputted[2]]-(i-1)]]])[numd[inputted[0:2]]]))).isalpha() != True:
				((gameboard[letd[rletd[letd[inputted[2]]-(i-1)]]])[numd[inputted[0:2]]]) = " "
			if ("{}".format(((gameboard[letd[rletd[letd[inputted[2]]-(i-1)]]])[numd[inputted[0:2]]+1]))).isalpha() != True:
				((gameboard[letd[rletd[letd[inputted[2]]-(i-1)]]])[numd[inputted[0:2]]+1]) = " "
			if ("{}".format(((gameboard[letd[rletd[letd[inputted[2]]-(i-1)]]])[numd[inputted[0:2]]+2]))).isalpha() != True:
				((gameboard[letd[rletd[letd[inputted[2]]-(i-1)]]])[numd[inputted[0:2]]+2]) = " "
			if ("{}".format(((gameboard[letd[rletd[letd[inputted[2]]-(i-1)]]])[numd[inputted[0:2]]+3]))).isalpha() != True:
				((gameboard[letd[rletd[letd[inputted[2]]-(i-1)]]])[numd[inputted[0:2]]+3]) = " "
			if ("{}".format(((gameboard[letd[rletd[letd[inputted[2]]-(i-1)]]])[numd[inputted[0:2]]+4]))).isalpha() != True:
				((gameboard[letd[rletd[letd[inputted[2]]-(i-1)]]])[numd[inputted[0:2]]+4]) = " "
			if ("{}".format(((gameboard[letd[rletd[letd[inputted[2]]-(i-1)]]])[numd[inputted[0:2]]+5]))).isalpha() != True:
				((gameboard[letd[rletd[letd[inputted[2]]-(i-1)]]])[numd[inputted[0:2]]+5]) = " "
			if ("{}".format(((gameboard[letd[rletd[letd[inputted[2]]+i]]])[numd[inputted[0:2]]]))).isalpha() != True:
				((gameboard[letd[rletd[letd[inputted[2]]+i]]])[numd[inputted[0:2]]]) = " "
			if ("{}".format(((gameboard[letd[rletd[letd[inputted[2]]+i]]])[numd[inputted[0:2]]-1]))).isalpha() != True:
				((gameboard[letd[rletd[letd[inputted[2]]+i]]])[numd[inputted[0:2]]-1]) = " "
			if ("{}".format(((gameboard[letd[rletd[letd[inputted[2]]+i]]])[numd[inputted[0:2]]-2]))).isalpha() != True:
				((gameboard[letd[rletd[letd[inputted[2]]+i]]])[numd[inputted[0:2]]-2]) = " "
			if ("{}".format(((gameboard[letd[rletd[letd[inputted[2]]+i]]])[numd[inputted[0:2]]-3]))).isalpha() != True:
				((gameboard[letd[rletd[letd[inputted[2]]+i]]])[numd[inputted[0:2]]-3]) = " "
			if ("{}".format(((gameboard[letd[rletd[letd[inputted[2]]-(i-1)]]])[numd[inputted[0:2]]]))).isalpha() != True:
				((gameboard[letd[rletd[letd[inputted[2]]-(i-1)]]])[numd[inputted[0:2]]]) = " "
			if ("{}".format(((gameboard[letd[rletd[letd[inputted[2]]-(i-1)]]])[numd[inputted[0:2]]-1]))).isalpha() != True:
				((gameboard[letd[rletd[letd[inputted[2]]-(i-1)]]])[numd[inputted[0:2]]-1]) = " "
			if ("{}".format(((gameboard[letd[rletd[letd[inputted[2]]-(i-1)]]])[numd[inputted[0:2]]-2]))).isalpha() != True:
				((gameboard[letd[rletd[letd[inputted[2]]-(i-1)]]])[numd[inputted[0:2]]-2]) = " "
			if ("{}".format(((gameboard[letd[rletd[letd[inputted[2]]-(i-1)]]])[numd[inputted[0:2]]-3]))).isalpha() != True:
				((gameboard[letd[rletd[letd[inputted[2]]-(i-1)]]])[numd[inputted[0:2]]-3]) = " "
		p1mins.mins -= building.cost
		for element in gameboard:
			print(("".join(element)).center(columns))
	else:
		print("You don't have enough minerals for that!".center(columns))
i = 0
while i == i:
	print("")
	print("You currently have: {} minerals.".format(p1mins.mins).center(columns))
	print(("What would you like to place? Buildings cost {} minerals, and units cost {} minerals. Input done if you're done.".format(100, 25)).center(columns))
	placetype = input("> ")
	if placetype == "u":
		unit()
	elif placetype == "b":
		build()
	elif placetype == "a":
		attack()
	elif placetype == "done":
		break
	else:
		print("Not a valid option!".center(columns))
		i += 1
print("")
print("Here is your board".center(columns))
for element in gameboard:
	print(("".join(element)).center(columns))