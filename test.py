import os
import paramiko

host = "192.168.0.252"
redunt = "192.168.0.253"
port = 22
ssh = paramiko.SSHClient()
UN = 1 #Read from file?
PW = 1 #Maybe, i dunno
trigger = 0

def ping(host):
	access = os.system("ping -c 1 " + host)
	if access == 0:
		return True
	else:
		return False

while trigger == 0:
	if ping(redunt) == True:
		print("Ok")
	else:
		print("WTF")
		ssh.connect(host, port, UN, PW)
		stdin, stdout, stderr = ssh.exec_command("int tun0")
		stdin, stdout, stderr = ssh.exec_command("no sh")
		trigger = 1

while trigger == 1:
	if access == True:
		ssh.connect(host, port, UN, PW)
		stdin, stdout, stderr = ssh.exec_command("int tun0")
		stdin, stdout, stderr = ssh.exec_command("sh")
		trigger = 0
