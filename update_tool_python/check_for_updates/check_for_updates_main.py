#!/usr/bin/python3

import os, sys
from ..common import updatemodule

# put the apt-check path here
aptCheckFile = "/usr/lib/update-notifier/apt-check"

def main(DATADIR):
  holderFile = DATADIR + "/updates.txt"
  zeroUpdateFile = DATADIR + "/zeroUpdates.txt"

  updatemodule.dependancies(aptCheckFile)
  updatemodule.checks(holderFile, zeroUpdateFile)
  updatemodule.zeroUpdates(zeroUpdateFile)
  updatemodule.update(aptCheckFile, holderFile, zeroUpdateFile)

if __name__ == "__main__":
  main(DATADIR)
