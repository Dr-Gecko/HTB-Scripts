import os
import sys
import getopt
empty = "" # Empty string so scripts can check for it

scriptmessage = """
        ██╗  ██╗████████╗██████╗     ██╗  ██╗███████╗██╗     ██████╗ ███████╗██████╗        
        ██║  ██║╚══██╔══╝██╔══██╗    ██║  ██║██╔════╝██║     ██╔══██╗██╔════╝██╔══██╗       
        ███████║   ██║   ██████╔╝    ███████║█████╗  ██║     ██████╔╝█████╗  ██████╔╝       
        ██╔══██║   ██║   ██╔══██╗    ██╔══██║██╔══╝  ██║     ██╔═══╝ ██╔══╝  ██╔══██╗       
        ██║  ██║   ██║   ██████╔╝    ██║  ██║███████╗███████╗██║     ███████╗██║  ██║       
        ╚═╝  ╚═╝   ╚═╝   ╚═════╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝       
                                                                                            
███╗██╗███╗    ██████╗  ██████╗  ██████╗     ██████╗ ███╗   ██╗██╗  ██╗   ██╗    ███╗██╗███╗
██╔╝██║╚██║    ██╔══██╗██╔═══██╗██╔════╝    ██╔═══██╗████╗  ██║██║  ╚██╗ ██╔╝    ██╔╝██║╚██║
██║ ██║ ██║    ██████╔╝██║   ██║██║         ██║   ██║██╔██╗ ██║██║   ╚████╔╝     ██║ ██║ ██║
██║ ╚═╝ ██║    ██╔═══╝ ██║   ██║██║         ██║   ██║██║╚██╗██║██║    ╚██╔╝      ██║ ╚═╝ ██║
███╗██╗███║    ██║     ╚██████╔╝╚██████╗    ╚██████╔╝██║ ╚████║███████╗██║       ███╗██╗███║
╚══╝╚═╝╚══╝    ╚═╝      ╚═════╝  ╚═════╝     ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝       ╚══╝╚═╝╚══╝
                                    Dr-Gecko 2022                                            """

helpmessage = scriptmessage + """


Usage:
  htb_helper.py <command> 

Commands:
  nmap                     Runs a nmap scan.
  gobuster                 Runs a gobuster directory scan
  
General Options:
  -h, --help                  Show help.
"""

def nmap():
    name=input("Enter Machine Name: ") # Enter the Name of the machine for the file name
    host=input("Enter Machine IP: ") # Enter the IP of the machine
    if host==empty:
        print("Please give a IP address for the machine")
        host=input("Enter Machine IP: ") # Enter the IP of the machine
    elif name==empty:
        print("Please enter a proper name for the machine ")
        name=input("Enter Machine Name: ") # Enter the Name of the machine for the file name
    command = "nmap -sV -sC -oN " + name + " " + host
    #os.system(command)
    print(command) # Debugging

def gobuster(): 
    host=input("Enter Machine IP: ") # Enter the IP of the machine
    wordlist=input("Enter path to wordlist, leave blank for default wordlist: ") # Wordlist selection 
    if wordlist==empty: # If wordlist is blank uses the default one
        wordlist="" 
    command="gobuster dir -u "+host+" "+" -w "+wordlist # Final Command 
    #os.system(command)
    print(command) # Debugging




# Dr-Gecko 2022