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

def killProcessByServiceOption(service, option1):
    #kill a process by a certain service and speciall option, such as 
    # kill process of 'dhclient eth0 '
    #cmd = ['pidof','dhclient']

    cmd = ['pidof', service]

    ret = Popen(cmd, stdout=PIPE, stderr=STDOUT).communicate()[0].decode('ascii')

    results = ret.strip().split()

    for pidstring in results:
        print(int(pidstring))
        processCmdl = psutil.Process(int(pidstring)).cmdline()
        if processCmdl[-1] == option1:
            print('--------{}{}'.format((ret[-1]),int(pidstring)))
            os.kill(int(pidstring), signal.SIGKILL)



if __name__=='__main__':
	ppid = 2560
	killByPid(ppid)

	killByService('dhclient')

	killprocess('dhclient', 'eth1')
