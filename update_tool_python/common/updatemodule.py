from pathlib import Path
from subprocess import call
import sys, os

# This method checks if holderFile and zeroUpdateFile exist, if they don't, it creates them
def checks(holderFile, zeroUpdateFile):
	if not Path(holderFile).is_file():
		call(["touch", holderFile])
	if not Path(zeroUpdateFile).is_file():
		call(["touch", zeroUpdateFile])

# This method checks if apt-check is installed
def dependancies(aptCheckFile):
	if not Path(aptCheckFile).is_file():
		print("You don't have apt-check installed, run \033[01;32msudo apt install update-notifier\033[00m\n\n")
		exit(2)

# This method sets the file zeroUpdates so it can be compared
def zeroUpdates(zeroUpdateFile):
	with open(zeroUpdateFile, 'w') as f:
		f.write("0 packages can be updated.\n0 updates are security updates.\n")

# This method does all the work, it runs apt-check and writes to a file for later use
def update(aptCheckFile, holderFile, zeroUpdateFile):
	try:
		with open(holderFile, 'w') as hf:
			call([aptCheckFile, "--human-readable"], stdout=hf)
	except ValueError:
		print("Unable to run apt-check and write to holder file")
		exit(2)
	else:
		with open(zeroUpdateFile, 'r') as zuf, open(holderFile, 'r') as hf:
			if zuf.readlines() != hf.readlines():
				with open(holderFile, 'a') as hf:
					hf.write("\nIf you want to update, run \033[01;32mupdater\033[00m\n")

def query(question, default="yes"):
	valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
	if default is None:
		prompt = " [y/n] "
	elif default == "yes":
		prompt = " [Y/n] "
	elif default == "no":
		prompt = " [y/N] "
	else:
		prompt = " [y/n] "

	while True:
		sys.stdout.write(question + prompt)
		choice = input().lower()
		if default is not None and choice == '':
			return valid[default]
		elif choice in valid:
			return valid[choice]
		else:
			sys.stdout.write("Please respond with 'yes' or 'no' "
					"(or 'y' or 'n').\n")

def updateFunction(section):
	if section == 1:
		print("\nRunning \033[01;32msudo apt update\n\033[00m (may ask for root)")
		try:
			call(["sudo", "apt", "update"])
		except ValueError:
			print("command \033[01;32msudo apt update\033[00m failed. Trying \033[01;32msudo apt-get update\033[00m\n")
			try:
				call(["sudo", "apt-get", "update"])
			except ValueError:
				print("command \033[01;32msudo apt-get update\033[00m failed, quitting")
				exit(2)
	elif section == 2:
		print("\nRunning \033[01;32msudo apt upgrade\033[00m\n")
		try:
			call(["sudo", "apt", "upgrade"])
		except ValueError:
			print("command \033[01;32msudo apt upgrade\033[00m failed. Trying \033[01;32msudo apt-get upgrade\033[00m\n")
			try:
				call(["sudo", "apt-get", "upgrade"])
			except ValueError:
				print("command \033[01;32msudo apt-get upgrade\033[00m failed, quitting")
				exit(2)
	elif section == 3:
		print("\nRunning \033[01;32msudo apt autoremove\033[00m\n")
		try:
			call(["sudo", "apt", "autoremove"])
		except ValueError:
			print("command \033[01;32msudo apt autoremove\033[00m failed. Trying \033[01;32msudo apt-get autoremove\033[00m\n")
			try:
				call(["sudo", "apt-get", "autoremove"])
			except ValueError:
				print("command \033[01;32msudo apt-get autoremove\033[00m failed, quitting")
				exit(2)

def getlink(file):
	if os.path.islink(file):
		path = os.path.dirname(os.readlink(file))
	else:
		path = os.path.dirname(file)
	return os.path.dirname(path)
