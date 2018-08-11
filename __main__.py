#!/usr/bin/env python3

from getpass import getpass

from personal_info import PersonalInfo


def main():
    gate = PersonalInfo(input('Username: '), getpass())
    print(gate.set_list(condition='CurrentAcadState=1'))
    print(gate.get_list(count=10, start=0))


if __name__ == '__main__':
    main()
