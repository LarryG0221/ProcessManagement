import signal
import multiprocessing
import os,threading
import time,sys

def signal_handler(num, stack):
    print ('Received signal %d in %s' % (num, threading.currentThread()))
    sys.exit(10)
    
def wait_for_signal():
    print ('Waiting for signal in', threading.currentThread())
    signal.pause()
    print ('Done waiting')

def send_signal():
    print ('Sending signal in', threading.currentThread())
    os.kill(os.getpid(), signal.SIGUSR1)


signal.signal(signal.SIGUSR1, signal_handler)
# Start a thread that will not receive the signal
receiver = threading.Thread(target=wait_for_signal, name='receiver')
receiver.start()

sender = threading.Thread(target=send_signal, name='sender')
sender.start()
#sender.join()

signal.signal(signal.SIGHUP, signal.SIG_IGN)
signal.alarm(2)
#receiver.join()



signal.signal(signal.SIGALRM, signal_handler)

def use_alarm():
    print( time.ctime(), 'Setting alarm in', threading.currentThread())
    print (time.ctime(), 'Sleeping in', threading.currentThread())
    time.sleep(3)
    print (time.ctime(), 'Done with sleep')

# Start a thread that will not receive the signal
alarm_thread = threading.Thread(target=use_alarm, name='alarm_thread')
alarm_thread.start()
time.sleep(2)

# Wait for the thread to see the signal (not going to happen!)
print (time.ctime(), 'Waiting for', alarm_thread)
alarm_thread.join()
signal.alarm(1)

print (time.ctime(), 'Exiting normally')