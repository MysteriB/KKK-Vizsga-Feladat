import os
import paramiko

host = "192.168.0.252"
redunt = "192.168.0.253"
port = 22
ssh = paramiko.SSHClient()
UN = 1 #Read from file?
PW = 1 #Maybe, i dunno
access = os.system("ping -c 1" + redunt)
trigger = 0

while trigger == 0:
	if access == 0:
		none
	else:
		ssh.connect(host, port, UN, PW)
		stdin, stdout, stderr = ssh.exec_command("int tun0")
		stdin, stdout, stderr = ssh.exec_command("no sh")
		trigger = 1

while trigger == 1:
	if access == 0:
		ssh.connect(host, port, UN, PW)
		stdin, stdout, stderr = ssh.exec_command("int tun0")
		stdin, stdout, stderr = ssh.exec_command("sh")
		trigger = 0
