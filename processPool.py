import multiprocessing 
import os 
import time
import psutil

def square(n): 
    print("Worker process id for {0}: {1}".format(n, os.getpid()))
    p = psutil.Process(os.getpid())
    print(p)
    n = 50000000
    while n>1:
        n-=1
    return (n*n)

if __name__ == "__main__": 
    # input list 
    mylist = [1,2,3,4,5] 
    time1=time.time()
    # creating a pool object 
    p = multiprocessing.Pool() 
    #p = multiprocessing.Process(target=square, args=(mylist,))
    #p.start()
    # map list to target function 
    result = p.map(square, mylist) 
    #p.join()
    print(time.time()-time1)