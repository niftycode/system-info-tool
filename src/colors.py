#!/usr/bin/env python3

"""
This class defines the colors for the foreground and background.
Version: 1.0
Python 3.12+
Date created: May 13th, 2024
Date modified: -
"""


class Colors:

    def __init__(self):
        pass

    @staticmethod
    def foreground(color, text):
        if color == "red":
            print(f"\033[95m{text}\033[0m")
            # return "\033[41m"
