#!/usr/bin/env python3

"""
Display various information about the operating system.
Version: 1.0
Python 3.12+
Date created: October 8th, 2024
Date modified: -
"""

import logging

# import os
import sys


from logging.config import fileConfig

from src import system_info


# Add logger config
fileConfig("logging.ini")
logger = logging.getLogger()


def print_magenta(text: str):
    """
    Outputs the text in purple color.

    Args:
        text: The text to display.
    """
    print(f"\033[35m{text}\033[0m")


def show_user_info():
    """
    Invokes the user system module.
    """
    print_magenta("User Info:")
    print_magenta("----------------------------------------------------------")
    system_info.fetch_user_info()


def show_system_info():
    """
    Invokes the system info module.
    """
    print_magenta("System Info:")
    print_magenta("----------------------------------------------------------")
    system_info.fetch_system_info()


def main():
    """
    Entry point of this application.
    """
    print()
    print("----------------------------------------------------------")
    print("Choose an option:")
    print()
    print("Show User Info: -1-")
    print("Show System Info: -2-")
    print("Exit program: -3-")
    print("----------------------------------------------------------")

    while True:
        choice = input("Your choice: ")

        if choice == "1":
            show_user_info()
            break
        elif choice == "2":
            show_system_info()
            break
        elif choice == "3":
            quit_application()
            break
        elif choice == "q":
            quit_application()
        else:
            print("Unknown input! Try again.")
            continue


def quit_application():
    """
    Quit application.
    """
    sys.exit("Goodbye!")


if __name__ == "__main__":
    main()
