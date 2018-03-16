theBoard = { 'top-L': ' ', 'top-M':' ', 'top-R':' ',
			'mid-L':' ', 'mid-M':' ', 'mid-R':' ',
			'low-L':' ', 'low-M':' ', 'low-R':' '}
win = False

def printBoard(theBoard):
	print('', theBoard['top-L'], '│', theBoard['top-M'], '│', theBoard['top-R'])
	print('───┼───┼───')
	print('', theBoard['mid-L'], '│', theBoard['mid-M'], '│', theBoard['mid-R'])
	print('───┼───┼───')	
	print('', theBoard['low-L'], '│', theBoard['low-M'], '│', theBoard['low-R'])

turn = 'X'
while True:
	printBoard(theBoard)
	if win == True:
		break


	print('Es el turno de', turn + '. ¿A qué espacio quieres moverte?')
	move = input()
	theBoard[move] = turn
	if theBoard['top-L'] == theBoard['top-M'] and theBoard['top-M'] == theBoard['top-R'] and theBoard['top-R'] != ' ' or \
	theBoard['mid-L'] == theBoard['mid-M'] and theBoard['mid-M'] == theBoard['mid-R'] and theBoard['mid-R'] != ' ' or \
	theBoard['low-L'] == theBoard['low-M'] and theBoard['low-M'] == theBoard['low-R'] and theBoard['low-R'] != ' ' or \
	theBoard['top-L'] == theBoard['mid-L'] and theBoard['mid-L'] == theBoard['low-L'] and theBoard['low-L'] != ' ' or \
	theBoard['top-M'] == theBoard['mid-M'] and theBoard['mid-M'] == theBoard['low-M'] and theBoard['low-M'] != ' ' or \
	theBoard['top-R'] == theBoard['mid-R'] and theBoard['mid-R'] == theBoard['low-R'] and theBoard['low-R'] != ' ' or \
	theBoard['top-L'] == theBoard['mid-M'] and theBoard['mid-M'] == theBoard['low-R'] and theBoard['low-R'] != ' ' or \
	theBoard['top-R'] == theBoard['mid-M'] and theBoard['mid-M'] == theBoard['low-L'] and theBoard['low-L'] != ' ':
		winner = turn
		win = True
	if turn == 'X':
		turn = 'O'
	else:
		turn = 'X'
print('¡El ganador del juego es', winner+'!')