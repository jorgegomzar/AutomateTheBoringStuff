import os
from sys import platform
from xml.dom import minidom

def clear():
	""" Clear function multi os """
	if platform == "linux":
		_ = os.system('clear')
	elif platform == "win32":
		_ = os.system('cls')

def macizer(mac):
	""" Formats input to look like a MAC address """
	newMac = []
	count = 0
	vecCount = [2, 4, 6, 8, 10]
	for c in mac:
		if count in vecCount:
			newMac.append(':')
		newMac.append(c)
		count = count + 1
	return ''.join(newMac)

def prettierString(id, mac):
	""" Converts the input into a prettier string """
	return ' [+] ID: {} | MAC: {}\n'.format(id, mac)

useIds = False
dictMAC = {}

if(input('¿Id? (s: sí): ').lower() == 's'):
	useIds = True

filename = str(input('Nombre de la red: '))

if not useIds:
	id_device = 1
else:
	id_device = input('ID: ')
# macAddr = macizer(input('MAC: '))
macAddr = input('MAC: ')

while  macAddr != '':
	clear()
	dictMAC[id_device] = macAddr
	print(prettierString(id_device, macAddr))

	if not useIds:
		id_device = id_device + 1
	else:
		id_device = input('ID: ')
	# macAddr = macizer(input('MAC: '))
	macAddr = input('MAC: ')

with open('./{}.txt'.format(filename), 'w') as file:
	for k, v in dictMAC.items():
		file.write(prettierString(k, v))

# with open('./{}.xml'.format(filename), 'w') as file:
	# XML IMPLEMENTATION

