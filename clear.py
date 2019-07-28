import sys
import os


def main(file):
    path = './database/' + file
    if os.path.exists(path):
        confirm = input('confirm clear?(y/n)')
        if confirm == 'y' or confirm == 'Y':
            open('./database/' + file, 'w')
        print('clear')
    else:
        print('can not find file')


if __name__ == '__main__':
    main(sys.argv[1])
