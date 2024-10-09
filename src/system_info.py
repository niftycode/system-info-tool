#!/usr/bin/env python3

"""
Version: 1.0
Python 3.12+
Date created: October 8th, 2024
Date modified: October 9th, 2024
"""

from uuid import getnode as get_mac

import os
import platform
import socket
import sys
import time

WINDOWS = "Windows"
MAC_OS = "Darwin"


def fetch_system_info():
    """
    Fetch system information
    """
    print("System Platform: ", sys.platform)
    print("Name: ", socket.gethostname())
    print("FQDN: ", socket.getfqdn())
    print("Node", platform.node())
    print("Platform: ", platform.platform())
    print("System OS: ", platform.system())
    print("Release: ", platform.release())
    print("Version: ", platform.version())
    print("Python Version: ", platform.python_version())
    if platform.system() == MAC_OS:
        print("macOS Version: ", platform.mac_ver()[0])
    print("Mac Address: ", hex(get_mac()))
    print("Platform architecture:", platform.architecture())
    print("Platform processor:", platform.processor())
    print("Machine type:", platform.machine())
    print("System's network name:", platform.node())


def fetch_user_info():
    """
    Fetch user information
    """
    if platform.system() != WINDOWS:
        user_identifier = os.getuid()  # type: ignore
        group = os.getgroups()  # type: ignore
        print("User number:", user_identifier)
        print("Group:", group)
    print("Process ID:", os.getpid())
    print("Login Name:", os.getlogin())
    print("Current Directory:", os.getcwd())
    print("Current Time: ", time.ctime(time.time()))

    if platform.system() == WINDOWS:
        system_env = os.environ

        # Show home directory
        print(f"Windows Directory: {system_env["WINDIR"]}")
