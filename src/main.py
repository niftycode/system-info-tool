#!/usr/bin/env python3

"""
Entry point of this program
Version: 1.0
Python 3.12
Date created: October 5th, 2023
Date modified: January 26th, 2024
"""

import logging
import os
# import pprint

from logging.config import fileConfig

from src import system_info

# Add logger config
fileConfig("logging.ini")
logger = logging.getLogger()


def main():
    system_env = os.environ

    print("System Info:")
    print("------------")
    system_info.fetch_system_info()

    print(system_env["SHELL"])

    print()
    print("User Info:")
    print("------------")
    system_info.fetch_user_info()
    '''
    system_env = os.environ
    # pprint.pprint(dict(system_env))

    # Show home directory
    print(system_env["HOME"])

    # Show user
    print(system_env["USER"])

    # Show language
    # print(system_env["LANG"])

    # Show used shell
    print(system_env["SHELL"])

    try:
        print(system_env["BASH"])
    except KeyError as e:
        print("ERROR: Environment variable does not exist!")
        print(e)

    # Or use get() instead of an exception handling.
    '''

if __name__ == '__main__':
    main()
