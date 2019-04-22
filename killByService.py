import os,signal
import subprocess
import psutil

def killByService(serviceName):

	cmd = ['pidof',serviceName]
	ret=subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0].decode('ascii')
	print(ret)
	for i in ret[:-1].strip().split():
    		print(int(i))
    		os.kill(int(i),signal.SIGKILL)


def killByPid(pid):
	ppid = 2560
	parent = psutil.Process(ppid)
	for child in parent.children(recursive=True):
    		print(child.pid)
    		child.kill()

	parent.kill()

if __name__=='__main__':
	ppid = 2560
	killByPid(ppid)

	killByService('dhclient')
