#!/usr/bin/env python3

import os

def main():
 if os.path.exists('./test/*.template.yaml'):
    print ("File Naming Standard Met = PASS")
 else:
    print ("Please Rename Following files to QuickStart Standard of *.template.yaml")
    arr = os.listdir('test')
    print(arr)


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (ValueError, TypeError):
        LOGGER.error(ValueError)

