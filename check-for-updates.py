#!/usr/bin/python3

import os, sys, updatemodule

# ToDo: Create a .conf file to hold this kind of data
# os.path.dirname(os.path.realpath()) will ignore symlinks
programRoot = os.path.dirname(os.path.realpath(sys.argv[0]))

# configure the files here, these should point to the installation directory
holderFile = programRoot + "/data/updates.txt"
zeroUpdateFile = programRoot + "/data/zeroUpdates.txt"

# put the apt-check path here
aptCheckFile = "/usr/lib/update-notifier/apt-check"

def main():
  updatemodule.dependancies(aptCheckFile)
  updatemodule.checks(holderFile, zeroUpdateFile)
  updatemodule.zeroUpdates(zeroUpdateFile)
  updatemodule.update(aptCheckFile, holderFile, zeroUpdateFile)

if __name__ == "__main__":
  main()
