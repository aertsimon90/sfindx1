import random, threading, socket, time, os
ss = []
ports = []
l = threading.Lock()
def tryfind():
	global ss, ports
	try:
		ip = str(random.randint(0, 255))+"."+str(random.randint(0, 255))+"."+str(random.randint(0, 255))+"."+str(random.randint(0, 255))
		port = random.choice(ports)
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(0.8)
		s.connect((ip, port))
		s.sendall("".encode())
		s.close()
		with l:
			ss.append(f"{ip}:{port}")
	except:
		pass
def botfind():
	while True:
		ts = []
		for _ in range(4):
			t = threading.Thread(target=tryfind)
			t.start()
			ts.append(t)
		for t in ts:
			t.join()
def sfthread(n):
	for _ in range(n):
		threading.Thread(target=botfind).start()
def savefile(filename):
	global ss
	while True:
		try:
			f = open(filename, "w")
			f.write("\n".join(ss))
			f.close()
			time.sleep(1)
		except:
			pass
def menu():
	global ss, ports
	os.system("clear")
	print("""\033[96m ____   __ _           ___  ___
/ ___| / _(_)_ __   __| \ \/ / |
\___ \| |_| | '_ \ / _` |\  /| |
 ___) |  _| | | | | (_| |/  \| |
|____/|_| |_|_| |_|\__,_/_/\_\_|
\033[93mSfindX1 - Server Finder Tool
        \033[96mby aertsimon90\033[0m""")
	print()
	bc = int(input("\033[96mEnter Bot Count (Standart=44): \033[93m"))
	ports = input("\033[96mEnter Ports (Example: 80/443): \033[93m")
	filename = input("\033[96mEnter File Name (Optional): \033[93m")
	ports = ports.replace("/", "").split()
	ports2 = []
	for port in ports:
		ports2.append(int(port))
	ports = ports2
	print("\033[96m\nStarting Bots...")
	sfthread(bc)
	print("Starting Auto File Saving...")
	threading.Thread(target=savefile, args=(filename,)).start()
	print("Sucessfuly!\n")
	while True:
		print(f"\033[96mCount Of Server Found: \033[93m{len(ss)}\033[0m")
		time.sleep(1)
while True:
	try:
		menu()
	except:
		print("\033[91mError")
		time.sleep(2.5)
