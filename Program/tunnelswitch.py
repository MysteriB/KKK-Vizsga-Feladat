import paramiko

host = "192.168.5.254"
port = 22
username = "verser"
password = "Mester"
conf = "conf t"
int = "int tunnel1"
nosh = "no sh"
sh = "sh"
enable = 1
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(ip, port, username, password)
    return True
except (BadHostKeyException, AuthenticationException, 
        SSHException, socket.error) as e:
    print e
    sleep(interval)

if enable == 0:
	ssh.connect(host, port, username, password)
	stdin, stdout, stderr = ssh.exec_command(conf)
	stdin, stdout, stderr = ssh.exec_command(int)
	stdin, stdout, stderr = ssh.exec_command(nosh)
	print("Redunt Tunnel Online)
if enbale == 1:
	ssh.connect(host, port, username, password)
	stdin, stdout, stderr = ssh.exec_command(conf)
	stdin, stdout, stderr = ssh.exec_command(int)
	stdin, stdout, stderr = ssh.exec_command(sh)
	print("Redunt Tunnel Offline)
