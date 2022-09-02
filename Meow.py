import telnetlib
import sys
HOST = input("enter your host IP:")
tn=telnetlib.Telnet(HOST)
x = tn.read_all()
print (x)