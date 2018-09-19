import os
from sys import platform

def clear():
	if platform == "linux":
		_ = os.system('clear')
	elif platform == "win32":
		_ = os.system('cls')

def macizer(mac):
	newMac = []
	count = 0
	vecCount = [2, 4, 6, 8, 10]
	for c in mac:
		if count in vecCount:
			newMac.append(':')
		newMac.append(c)
		count = count + 1
	return ''.join(newMac)

def write2file(f, id, mac):
	cadena = ' [+] ID: ' + id + ' | MAC: ' + mac + '\n'
	f.write(cadena)
	print(cadena)

useIds = False
if(input('¿Id? (s: sí): ').lower() == 's'):
	useIds = True

folder = str(input('Nombre de la red: '))
os.mkdir(folder)

file = open('./'+folder+'/listadoMac.txt', 'w')
if not useIds:
	id_device = 1
else:
	id_device = input('ID: ')
macAddr = macizer(input('MAC: '))
while  macAddr != '':
	clear()
	write2file(file, str(id_device), macAddr)
	if not useIds:
		id_device = id_device + 1
	else:
		id_device = input('ID: ')
	macAddr = macizer(input('MAC: '))	
file.close()