# This script contains commands and functions to get a base system diagnostic.
# Created By: Kendall Davenport. Last Updated: 13 November 2021.
#I have imported the following libraries to preform specific tasks.
import getpass
import socket
import sys
import platform
import os
import ctypes


#I this is the main function
def Snoop():
    """
    This function will see will check if it is on a VM or not
    Afterwards it will check what system it is on using the uname function
    I then have the option to terminate the script, or keep snooping, depending on user preferance
    """
    # I have all my veriables diffined here
    operating_sys = platform.system()
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    user = getpass.getuser()

    # This is a try attempt to check if user has Admin rights
    if operating_sys == "Windows":
        is_sudo = None
        try:
            is_admin = os.getuid() == 0
        except AttributeError:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        else: is_admin = False

    # Same as prior if statement, but for Sudo rights
    if operating_sys != "Windows":
        is_admin = None
        test_sudo = os.system("sudo -S /bin/chmod --help >/dev/null 2>&1")
        if test_sudo == 0:
            is_sudo = True
        else:
            is_sudo = False

    # This if statement looks at the os and draws a line
    if platform.system() == "Windows":
        print('_' * 100)
    elif operating_sys == "Darwin":
        print('_' * 100)
    elif operating_sys == "Linux":
        print('_' * 100)
    elif operating_sys == "Java":
        print('_' * 100)
    else:
        print("ERROR: Unable to verify system's os.")

    # This checks weither or not the machine in use is a vm or not.
    if sys.prefix == sys.base_prefix:
        print(f'This is a real machine\nRunning on {operating_sys} operating system.\n')
    else:
        print(f'This is a virtual machine\nRunning on {operating_sys} operating system.\n')

    # This print statement gives me the os, node, release, version, and machine.
    print(f"Here are some of the system's specs: \n\t*Node:{platform.node()}\n\t*Version:{platform.version()}"
          f"\n\t*Release:{platform.release()}\n\t*Machine:{platform.machine()}"
          f"\n\t*IPv4:{local_ip}\n\t*User:{user}\n\t*Admin:{is_admin}\n\t*Sudo:{is_sudo}")

    # This prints another line, then gives commonly used commands for your os.
    if platform.system() == "Windows":
        print('_' * 100)
        print("Here are some commonly used commands for Windows:\n"
              "\t*ipconfig - gives IP and connections\n"
              "\t*ping [IP destination] - tests connection\n"
              "\t*chkdsk - checks disk\n"
              "\t*sfc - (system file checker) used to check file integrity\n"
              "\t*tree - shows file paths\n"
              "\t*CD [location] - Change Directory\n"
              "\t*netstat - gives network run-up\n"
              "\t*cls - clears the cmd")
        print('_' * 100)

    elif operating_sys == "Darwin":
        print('_' * 100)
        print("Here are some commonly used commands for Macs:\n"
              "\t*ls - see current directory\n"
              "\t*cd [location] - move to location directory\n"
              "\t*cp - coppies file\n"
              "\t*rm - deletes file\n"
              "\t*ping [IP] - test connection\n"
              "\t*sudo [cmd] - potentially elivates to super user permission")
        print('_' * 100)

    elif operating_sys == "Linux":
        print('_' * 100)
        print("Here are some commonly used commands for Linux:\n"
              "\t*ls - see current directory\n"
              "\t*cd [location] - move to location directory\n"
              "\t*cp - coppies file\n"
              "\t*rm - deletes file\n"
              "\t*ping [IP] - test connection\n"
              "\t*sudo [cmd] - potentially elivates to super user permission")

    elif operating_sys == "Java":
        print('_' * 100)
        print("Here are some commonly used commands for Java:\n"
              "\t*ls - see current directory\n"
              "\t*cd [location] - move to location directory\n"
              "\t*cp - coppies file\n"
              "\t*rm - deletes file\n"
              "\t*ping [IP] - test connection\n"
              "\t*java - list of all java cmds")

    else:
        print("ERROR: Unable to verify system's os.")

# This runs main function on startup
Snoop()
