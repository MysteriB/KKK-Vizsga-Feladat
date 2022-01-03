import paramiko
import time

UN = input("Username : ")
PW = input("Password : ")


host = "192.168.1.12"
port = 22
i = 0
#copy running-config ftp
#localip
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, UN, PW)
while i < 1:
    command = input("command : ")
    if command == "exit":
        i = 1
    else:
        command = "paru -S openspades"
        stdin, stdout, stderr = ssh.exec_command(command)
        lines = stdout.readlines()
        print(lines)
        command = "Y"
        stdin, stdout, stderr = ssh.exec_command(command)
        lines = stdout.readlines()
        print(lines)