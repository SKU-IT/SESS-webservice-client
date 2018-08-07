#!/usr/bin/env python3

from getpass import getpass

from sess import SESS


def main():
    sess = SESS(input('Username: '), getpass(), 'StdService')
    sess.login(gate='test')
    print(sess.set_list(condition=''))
    print(sess.get_list(count=10, start=0))


if __name__ == '__main__':
    main()
