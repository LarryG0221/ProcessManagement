import os,psutil
import signal

def killprocessByProcessCmd(arg1,arg2):
	cmd = ['pidof', arg1]
	ret = Popen(cmd, stdout=PIPE, stderr=STDOUT).communicate()[0].decode('ascii')
	results = ret.strip().split()
	for pidstring in results:
		print(int(pidstring)
		processCmdl = psutil.Process(int(pidstring)).cmdline()

		if processCmdl[-1] == arg2:
			os.kill(int(pidstring), signal.SIGKILL)

if __name__ == '__main__':
	killprocess('dhcilent','eth1')
