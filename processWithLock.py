from multiprocessing import Process, Lock

import os
import time

def info(title):
    print (title)
    print ('module name:', __name__)
    if hasattr(os, 'getppid'):  # only available on Unix
        print ('parent process:', os.getppid())
    print ('process id:', os.getpid())

def greeting(lock,name,t1):
    #info('function f')
    lock.acquire()

    for i in range(5):
        print ('hello', name)
        
        time.sleep(t1)
    lock.release()

if __name__ == '__main__':
    #info('main line')
    '''lock = Lock()
    p1 = Process(target=greeting, args=(lock,'bob',2))
    p2 = Process(target=greeting, args=(lock,'susan',1))
    p1.start()
    p1.join()
    p2.start()
    p2.join()
    '''
    for i in range(5):
        print('bob print....')
        for j in range(5):
            print('Susan printing...')
            time.sleep(.2)
        
