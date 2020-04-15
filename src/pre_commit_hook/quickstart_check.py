#!/usr/bin/env python3
import fnmatch
import os
import sys
import logging

LOGGER = logging.getLogger()
def main():
 file = sys.argv[1]
 if fnmatch.fnmatch(file, '*.template.yaml'):
    print ("File Naming Standard Met = PASS")
 else:
    print ("Please Rename Following files to QuickStart Standard of *.template.yaml")
    #arr = os.os.path.isfile(file)
    print(file)



if __name__ == '__main__':
    try:
        sys.exit(main())
    except (ValueError, TypeError):
        LOGGER.error(ValueError)

