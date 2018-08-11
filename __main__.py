#!/usr/bin/env python3

from getpass import getpass

from personal_info import PersonalInfo


def main():
    gate = PersonalInfo(input('Username: '), getpass())
    print(gate.get_data('CurrentAcadState=1', max_length=10))


if __name__ == '__main__':
    main()
