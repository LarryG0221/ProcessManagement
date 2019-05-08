import os, sys,time 
import signal

'''
childpid = os.fork()
print('childpid is ...', childpid)
def sighandler(signum, frame):
    print('handling the signal')
    spid = os.getpid()

    print('process id ', spid)

if childpid:
    print('parent  pausing', childpid)
    time.sleep(5)
    os.kill(childpid, signal.SIGUSR1)
else:
    print('child', childpid)
    signal.signal(signal.SIGUSR1,sighandler)
    time.sleep(10)
'''
print('----------')
workers=[]
for i in range(3):
    print ('PARENT: Forking %s' % i)
    worker_pid = os.fork()
    if not worker_pid:
        print( 'WORKER %s: Starting' % i)
        print ('WORKER %s: Finishing' % i)
        sys.exit(i)
    workers.append(worker_pid)

for i in workers:
    print ('PARENT: Waiting for %s' % i)
    done= os.waitpid(i,0)
    print ('PARENT:', done)



os.spawnlp(os.P_WAIT, 'ls', 'ls', '-l', '/tmp/')
print('0000000')