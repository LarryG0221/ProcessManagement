from multiprocessing import Pool,Process,Queue, Pipe, Lock,Manager
import os
from multiprocessing import Pool, TimeoutError

def info(title):
    print (title)
    print ('module name:', __name__)
    if hasattr(os, 'getppid'):  # only available on Unix
        print ('parent process:', os.getppid())
    print ('process id:', os.getpid())

def f(name):
    info('function f')
    print ('hello', name)

def fun_q(q):
    q.put([42, None, 'hi'])

def fun_pipe(conn):
    conn.send({'abc':'xyz'})
    print ('process id:', os.getppid(), os.getpid())
    conn.close()

def fun_lock(lock, cnt):
    lock.acquire()

    print('this is the {} one'.format(cnt))
    lock.release()

def fun_manager(d,l):
    d['city'] = 'beijing'
    d['code'] = '10101'
    d['type']='simple'

    l.reverse()

def fun_pool(x):
    return x * 10


if __name__ == '__main__':
    '''info('main line')

    p = Process(target=f, args=('bob',))
    p1 = Process(target=info, args=('title2',))

    p.start()
    p1.start()
    p.join()
    p1.join()
   
    q = Queue()
    p = Process(target=fun_q, args=(q,))
    p.start()
    print(q.get()[0])
    p.join()
   
    print ('main process id:', os.getppid(), os.getpid())

    parent_conn, child_conn = Pipe()

    p = Process(target = fun_pipe, args= (child_conn,))
    p.start()
    print(parent_conn.recv())

    p.join()
    p.terminate()
    

    lock = Lock()

    for i in range(10):
        p = Process(target = fun_lock, args = (lock,i))
        p.start()
        p.join()
    
    manager = Manager()

    d = manager.dict()
    l = manager.list(range(10))
    print(d)
    print(l)

    p = Process(target = fun_manager, args=(d,l))
    p.start()
    p.join()

    print(d)
    print(l)
    '''

    pool = Pool(processes =4)

    print (pool.map(fun_pool, range(10)))

    unorderlist = list( i for i in pool.imap_unordered(fun_pool, range(10)))
    print(unorderlist)
