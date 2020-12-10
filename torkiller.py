import os
import time
from subprocess import check_output
def get_pid(name):
    return check_output(["pidof",name])

while True:
	time.sleep(1)
	try:
		pid = (int(get_pid("tor")))
		print(pid)
		os.system("kill "+str(pid))
	except:
		print("Tor is not running!")
