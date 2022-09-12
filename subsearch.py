import requests
import re
from multiprocessing.dummy import Pool
import os
requests.packages.urllib3.disable_warnings()

def banner():
	G = '\033[92m'  # green
	Y = '\033[93m'  # yellow
	B = '\033[94m'  # blue
	R = '\033[91m'  # red
	W = '\033[0m'   # white
	
	print("""%s

			           _     __                     _     
			 ___ _   _| |__ / _\ ___  __ _ _ __ ___| |__  
			/ __| | | | '_ \\\ \ / _ \/ _` | '__/ __| '_ \ 
			\__ \ |_| | |_) |\ \  __/ (_| | | | (__| | | |
			|___/\__,_|_.__/\__/\___|\__,_|_|  \___|_| |_|%s%s                      

		\t# Coded by c0derzhax0r - @lifznotes
			""" % (R, W, Y))


def single():

	nama = input('[-] Scan Website : ')
	if '://' in nama:
		oke = nama.split('/')
		web = oke[2]
	else:
		web = nama
	web = web.replace('www.', '')

	r = requests.get('https://sonar.omnisint.io/subdomains/{}'.format(web), verify=False)
	ambil = re.findall('"(.*?)"', r.text)

	if r.status_code == 200:
		print('\n' + '\033[94m' + '[-] ' + 'Ditemukan Sub Domain dari ', web + ' :')
		for a in ambil:
			print('\033[92m' + '[-]' + ' ' + a)
	else:
		print('No Record!')


def mass(hola):

	if '://' in hola:
		oke = hola.split('/')
		websit = oke[2]
	else:
		websit = hola
	websit = websit.replace('www.', '')

	r = requests.get('https://sonar.omnisint.io/subdomains/{}'.format(websit), verify=False)
	jupuk = re.findall('"(.*?)"', r.text)

	if r.status_code == 200:
		print(websit, '|', len(jupuk), 'Subdomains')
		for b in jupuk:
			le = b.strip()
			open('subdo.txt', 'a').write('\n'+le+'\n')
	else:
		print(websit, '| Sub domain tidak ditemukan!')

def thread(ok):

	geh = open(ok, 'r').read().splitlines()
	p = Pool(50)
	p.map(mass, geh)


if __name__ == "__main__":

	os.system('cls' if os.name == 'nt' else 'clear')
	banner()
	print('\033[94m' + 'Menu yang tersedia : ')
	print('\033[94m' + '[1] Single Scanner')
	print('\033[94m' + '[2] Mass Scanner'+'\n')

	pilih = input('\033[91m' + '[-] Pilih Menu : ')

	if pilih == '1':
		single()
	elif pilih == '2':
		webmu = input('[-] Masukan list website : ')
		thread(webmu)
	else:
		print('Pilihan tidak valid!')
