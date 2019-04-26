
import time
import multiprocessing

def f(ns):

    ns.put(4)

if __name__ == '__main__':
    q = multiprocessing.Queue()
    q.put(1)
    

    while  not q.empty():
        print( 'before', q.get() )

    p = multiprocessing.Process(target=f, args=(q,))
    p.start()
    p.join()
    while  not q.empty():
        print( 'after', q.get() )
    
    