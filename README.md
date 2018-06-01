# update-tool-python
The same tool as my update-tool, but this one uses Python instead of BASH.

So far this tool contains two scripts, written in Python3. Since this tool is designed only to assist in the Apt platform (ubuntu and some debian systems), it will be strictly available for those systems.

The Problem: I have several Ubuntu-Based distributions that have their own MOTD when each user logs in. I need to be able to show available updates when someone logs in, so that they know if any packages need updating. apt-check (part of update-notifier) can provide this functionality, but it can slow down the login process depending on network speed - because apt-check has to connect to the canonical server to check for updates to aptitude packages. Sometimes, a user would open the terminal and the terminal would appear to hang for 2-3 seconds before the MOTD finally pops up.

The Solution: Create a script that calls for apt-check periodically (such as once per day, as a Cron-job) and updates a file, somewhere on the system, that contains the pre-formatted "update" text - which can be added into the MOTD.

The Solution's Problem: This makes a problem where, if you see that you have updates and you update by running apt update/upgrade, the next time you log in the script may not have run and the system will still tell you that you have updates.

The Solution's Problem's Solution: So I created two scripts. The update-checker, and a custom update-helper - all the update-helper does is assist in the process of going through aptitude to update the out of date packages. However, to assist in user-usability, it makes calls back to the update-checker so that there are no gaps left in the system.

Dependancies:
1. Apt - built into ubuntu. Canonical installation package
2. Python3 - Python3 is required for the apt-check script as well as this script. (sudo apt install python)
3. update-notifier - update-notifier is required because it contains the apt-check script. (sudo apt install update-notifier)

Installation:
1. Make the file "install" executable by doing 'chmod +x install'
2. run the command "sudo ./install" from the clone directory, the script should take care of the rest. If it doesn't, take a look in the "install" script (it is a shell script).

Uninstallation:
1. Make the file "uninstall" executable by doing 'chmod +x uninstall'
2. The script "install" will create a text file named install-record.txt, this file contains all the items that were installed. Run "sudo ./uninstall" to automatically remove all these items.
