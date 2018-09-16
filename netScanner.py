import os

def validate_ip(s):
	"""Si la cadena pasada como parámetro es una dirección ip devuelve True
	si no lo es devuelve False
	"""
	a = s.split('.')
	if len(a) != 4:
		return False
	for x in a:
		if not x.isdigit():
			return False
		i = int(x)
		if i < 0 or i > 255:
			return False
	return True
def networkGuess():
	"""Consigue la dirección de la red actual haciendo uso de herramientas del sistema
	"""
	ip_red = ''

	os.system('arp -a > arp.txt')
	archivo = open('arp.txt', 'r')

	while True:
		linea = archivo.readline().lstrip('  ')
		if validate_ip(linea[:11]):
			archivo.close()
			os.system('del arp.txt')
			return linea[:10]+'0'
		if linea == '':
			break

	archivo.close()
	os.system('del arp.txt')

def nmapScanner(dir_ip):
	"""A partir de la dirección ip de la red actual realiza el escaneo de toda ésta
	asumiendo que es de clase C, en busca de dispositivos y devuelve la información
	relevante
	"""
	os.system('nmap -sP '+ dir_ip +'/24 > listado.txt')
	archivo = open('listado.txt', 'r')
	router = False
	while True:
		linea = archivo.readline()
		if 'Host is up' not in linea and 'Nmap done' not in linea and 'Starting' not in linea and 'Finished' not in linea and '' != linea and '\n' != linea:
			linea = linea.lstrip('Nmap scan report for').rstrip('\n')
			if validate_ip(linea):
				if not router:
					router = True
					ip_router = linea
				print('[+] '+linea.rstrip('\n')+':')
			else:
				print(linea)
		if linea == '':
			break
	archivo.close()
	os.system('del listado.txt')
	return ip_router



# Inicio del programa
os.system('echo off')
red = networkGuess()
print('La red actual es la', red)
if (input('¿Deseas realizar un escaneo de la red en busca de dispositivos? (s/n) ') == 's'):
	os.system('cls')
	router = nmapScanner(red)
	print('\nLa dirección del gateway es la ' + router)
else:
	print('Adiós.')

