#!/usr/bin/env python3

from getpass import getpass

from sess import StdService


def main():
    std_service = StdService(input('Username: '), getpass())
    std_service.login(gate='test')
    print(std_service.set_list(condition=''))
    print(std_service.get_list(count=10, start=0))


if __name__ == '__main__':
    main()
