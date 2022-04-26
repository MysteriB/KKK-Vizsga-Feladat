import paramiko
import time

host = "100.0.0.14"
ip = "192.168.1.252"
port = "22"
username = "verser"
password = "Mester"
conf = "conf t\n"
interface = "int tunnel 1\n"
nosh = "no shutdown\n"
sh = "sh\n"
over = "end\n"
enable = 0
ssh = paramiko.SSHClient()
test = 0



while True:
    while test == 0:
        for x in range(1):
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                ssh.connect(hostname=ip, username=username, password=password, port=port, look_for_keys=False, allow_agent=False, timeout=3)
                print("RouterB is Online")
            except:
                test = 1
                ssh.connect(hostname=host, username=username, password=password, port=port, look_for_keys=False, allow_agent=False)
                conn = ssh.invoke_shell()
                conn.send(conf)
                time.sleep(.5)
                conn.send(interface)
                time.sleep(.5)
                conn.send(nosh)
                time.sleep(.5)
                conn.send(over)
                print("RouterB is Offline")
                print("Redunt Tunnel Online")
                ssh.close()
            time.sleep(30)
    while test == 1:
        for x in range(1):
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                ssh.connect(hostname=ip, username=username, password=password, port=port, look_for_keys=False, allow_agent=False, timeout=3)
                time.sleep(1)
                print("Back Online")
                enable = 1
            except:
                print("Waiting for RouterB...")
            if enable == 1:
                test = 0
                ssh.connect(hostname=host, username=username, password=password, port=port, look_for_keys=False, allow_agent=False, timeout=3)
                conn = ssh.invoke_shell()
                conn.send(conf)
                time.sleep(.5)
                conn.send(interface)
                time.sleep(.5)
                conn.send(sh)
                time.sleep(.5)
                conn.send(over)
                print("RouterB Online")
                print("Redunt Tunnel Offline")
                ssh.close()
            time.sleep(30)