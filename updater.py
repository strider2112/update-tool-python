#!/usr/bin/python3
import os, sys
from updatemodule import query, updateFunction

programRoot = os.path.dirname(os.path.realpath(sys.argv[0]))

updateFile = programRoot + "/data/updates.txt"
updateChecker = programRoot + "check-for-updates.py"

def main():
	with open(updateFile) as uf:
		lines = [line.rstrip('\n') for line in uf]
	print(lines[0])
	print(lines[1])

	if not query("Do you still want to update?","yes"):
		exit()
	updateFunction(1)
	if not query("Continue with \033[01;32msudo apt upgrade\033[0m?","yes"):
		exit()
	updateFunction(2)
	if not query("\nUpdate complete, there may be leftover files, do you want to run autoremove?"):
		exit()
	updateFunction(3)

if __name__ == "__main__":
	main()
