#!/usr/bin/python3
import os, sys
from ..common.updatemodule import query, updateFunction

def main(DATADIR, DIR):
	updateFile = DATADIR + "/updates.txt"
	updateChecker = DIR + "check_for_updates.py"

	with open(updateFile) as uf:
		lines = [line.rstrip('\n') for line in uf]
	print(lines[0])
	print(lines[1])

	if not query("\nDo you still want to update?","yes"):
		exit()
	updateFunction(1)
	if not query("\nContinue with \033[01;32msudo apt upgrade\033[0m?","yes"):
		exit()
	updateFunction(2)
	if not query("\nUpdate complete, there may be leftover files, do you want to run autoremove?"):
		exit()
	updateFunction(3)

if __name__ == "__main__":
	main(DATADIR, DIR)
