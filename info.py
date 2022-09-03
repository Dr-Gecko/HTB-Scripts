import os
# [*]=================_Messages_=================[*]
headermessage = """
 ██████╗ ███████╗ ██████╗██╗  ██╗███████╗ ██████╗██████╗ ██╗██████╗ ████████╗
██╔════╝ ██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔════╝██╔══██╗██║██╔══██╗╚══██╔══╝
██║  ███╗█████╗  ██║     █████╔╝ ███████╗██║     ██████╔╝██║██████╔╝   ██║   
██║   ██║██╔══╝  ██║     ██╔═██╗ ╚════██║██║     ██╔══██╗██║██╔═══╝    ██║   
╚██████╔╝███████╗╚██████╗██║  ██╗███████║╚██████╗██║  ██║██║██║        ██║   
 ╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝   
                    HackTheBox Made Easy By Dr-Gecko 2022
"""
meowmessage = """
Category: Starting Point
Box name: Meow
Difficulty: Very easy
Tools required: Telnet
Tags: Telnet, Enumeration, External, Penetration Tester Level 1"""

fawnmessage = """
Category: Starting Point
Box name: Fawn
Difficulty: Very easy
Tools required: FTP
Tags: External, Penetration Tester Level 1, Enumeration, FTP"""
# [*]=================_Functions_=================[*]
def open_flag():
    os.system("cat flag.txt")