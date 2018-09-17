import os

def write2file(f, id, mac):
	f.write(' [+] ID: ' + id + ' | MAC: ' + mac + '\n')

folder = input('Nombre de la red: ')
os.system('mkdir ' + folder)
file = open('./'+folder+'/listadoMac.txt', 'w')
id_device = input('ID: ')
while id_device != '':
	macAddr = input('MAC: ')
	write2file(file, id_device, macAddr)
	os.system('cls')
	id_device = input('ID: ')

file.close()