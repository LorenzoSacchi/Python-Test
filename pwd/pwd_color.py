#! /usr/local/bin/python3

import os


def main():
    home = os.getenv('HOME').split(sep='/')
    path = os.getcwd().split(sep='/')
    if home == path[:3]:
        path[2] = '\033[1;96m~'
        del path[0]
        del path[0]
    print(*path,sep='\033[1;35m/\033[1;96m')


if __name__ == "__main__":
    main()
