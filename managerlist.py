"""
from multiprocessing import Process,Manager

def f1(args1):
    args1.x =3
    print(args1)

if __name__=='__main__':
    with Manager() as mg:
        args0 = mg.Namespace()
        
    args0.x = 10
    p = Process(target=(f1), args=(args0,),daemon=True)
    p.start()
    p.join()

    print(args0)
"""
import time
import multiprocessing 

def f(ns):

    ns.pop()

if __name__ == '__main__':
    manager = multiprocessing.Manager()
    ns = manager.list([1,2,4])
    

    print( 'before', ns)
    p = multiprocessing.Process(target=f, args=(ns,))
    p.start()
    p.join()
    print ('after', ns)
    p = multiprocessing.Process(target=time.sleep, args=(1000,))
    p.start()
    print('werwerwe')
    