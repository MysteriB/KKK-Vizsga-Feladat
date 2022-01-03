import paramiko
import time
from host import network_devices
from config import host_conf


UN = input("Username : ")
PW = input("Password : ")


host = "192.168.1.12"
port = 22
command = "copy ftp startup"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, UN, PW)
stdin, stdout, stderr = ssh.exec_command(command)
lines = stdout.readlines()
print(lines)