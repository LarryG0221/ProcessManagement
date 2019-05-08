import multiprocessing
import time
import signal
import os
import sys

def handler2(signal, frame):
    print("handler!!!")
    sys.exit(10)

def handler1(signal, frame):
    print("handler11111111!!!")
    sys.exit(10)

def worker(): 
    p = multiprocessing.current_process()
    try:
        signal.signal(signal.SIGTERM,handler)  

        print("[PID:{}] acquiring resources".format(p.pid))
        while(True):           
            #working...
            time.sleep(0.5)
    except (KeyboardInterrupt, SystemExit):
        pass
    finally:
        print("[PID:{}] releasing resources".format(p.pid))

def handler(signum, frame):
    print('signal handler handed with %s'%signal)
    raise OSError('cannot open device')


if __name__ == "__main__":
    
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(4)

    fd = os.open('/dev/ttys0', os.O_RDWR)
    signal.alarm(0)

    """cd
    p = multiprocessing.Process(target=worker)
    p.start()

    time.sleep(3)      
    os.kill(p.pid,signal.SIGTERM)
    p.join()
    print(p)
    print(p.exitcode)
    print("joined all processes")
    """