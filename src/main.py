#!/usr/bin/env python3

"""
Entry point of this program
Version: 1.0
Python 3.12
Date created: October 5th, 2023
Date modified: June 2nd, 2024
"""

import logging
import os


from logging.config import fileConfig

from src import system_info


# Add logger config
fileConfig("logging.ini")
logger = logging.getLogger()


def print_magenta(text: str):
    """
    Outputs the text in purple color
    :param text: The text to display
    """
    print(f"\033[35m{text}\033[0m")


def main():
    system_env = os.environ

    print()
    print_magenta("System Info:")
    print_magenta("-----------------------------------------")
    system_info.fetch_system_info()

    print(f"Login Shell: {system_env["SHELL"]}")

    print()
    print_magenta("User Info:")
    print_magenta("-----------------------------------------")
    system_info.fetch_user_info()
    """
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
    """


if __name__ == "__main__":
    main()
