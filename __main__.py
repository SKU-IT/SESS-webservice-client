#!/usr/bin/env python3

from getpass import getpass

from sess import SESS


def main():
    sess = SESS(input('Username: '), getpass())


if __name__ == '__main__':
    main()
