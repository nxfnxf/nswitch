import random
import getpass
import time
import threading
import os
import subprocess
import signal
from termcolor import colored

def start():
	vpns = os.listdir(DIR)
	vpns.remove("switch.py")
	os.popen("printf \"" + USERNAME + "\n" + PASSWORD + "\" > config.txt")
	vpns.remove("config.txt")
	while True:
		try:
			p = subprocess.Popen("sudo openvpn --script-security 2 --config " + vpns[random.randint(0, len(vpns))] + " --auth-user-pass " + DIR + "config.txt", shell=True, preexec_fn=os.setsid)
			print("VPN Changed successfully.")
			time.sleep(int(INTERVAL))
			p.kill()
			os.killpg(os.getpgid(p.pid), signal.SIGTERM)
			time.sleep(5)
		except KeyboardInterrupt:
			os.killpg(os.getpgid(p.pid), signal.SIGTERM)
			sys.exit(0)

INTERVAL = 30
DIR = "/home/" + os.environ['USER'] + "/vpn/"

print colored("\n\n888b    888 .d8888b. 888       888888888888888888888 .d8888b. 888    888", "red")
print colored("8888b   888d88P  Y88b888   o   888  888      888    d88P  Y88b888    888", "red")
print colored("88888b  888Y88b.     888  d8b  888  888      888    888    888888    888", "red")
print colored("888Y88b 888 \"Y888b.  888 d888b 888  888      888    888       8888888888", "red")
print colored("888 Y88b888    \"Y88b.888d88888b888  888      888    888       888    888", "red")
print colored("888  Y88888      \"88888888P Y88888  888      888    888    888888    888", "red")
print colored("888   Y8888Y88b  d88P8888P   Y8888  888      888    Y88b  d88P888    888", "red")
print colored("888    Y888 \"Y8888P\" 888P     Y8888888888    888     \"Y8888P\" 888    888\n", "red")

inp1 = raw_input("Enter configuration (leave empty for default value)\nInterval to use (in seconds): ")
if(inp1 != ""):
	INTERVAL = inp1

inp2 = raw_input("Directory to OpenVPN conf. files: ")
if(inp2 != ""):
	DIR = inp2
USERNAME = raw_input("Enter login username to use: ")
PASSWORD = getpass.getpass("Enter password to use: ")

raw_input("All configurations set. Press enter to start...")

start()
