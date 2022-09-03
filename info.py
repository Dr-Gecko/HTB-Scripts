Your_Username_Here = "Dr-Gecko"

# [*]=================_Messages_=================[*]
headermessage = """
 ██████╗ ███████╗ ██████╗██╗  ██╗███████╗ ██████╗██████╗ ██╗██████╗ ████████╗
██╔════╝ ██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔════╝██╔══██╗██║██╔══██╗╚══██╔══╝
██║  ███╗█████╗  ██║     █████╔╝ ███████╗██║     ██████╔╝██║██████╔╝   ██║   
██║   ██║██╔══╝  ██║     ██╔═██╗ ╚════██║██║     ██╔══██╗██║██╔═══╝    ██║   
╚██████╔╝███████╗╚██████╗██║  ██╗███████║╚██████╗██║  ██║██║██║        ██║   
 ╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝   
                    HackTheBox Made Easy By Gecko
"""
meowmessage = """
Category: Starting Point
Box name: Meow
Difficulty: Very easy
Tools required: Telnet
Tags: Telnet, Enumeration, External, Penetration Tester Level 1"""

# [*]=================_Functions_=================[*]

default = "Username Not Added"
if Your_Username_Here == default:
    unencoded = "ERR, USERNAME NOT ADDED. Check GeckScript/README.MD for how to fix"
else:
    unencoded = "echo 'Pwned by " + Your_Username_Here + " with GeckScript!' >> flag.txt"
Hacked_Message_As_Bytes = str.encode(unencoded)
print(Hacked_Message_As_Bytes)