from multiprocessing import Process, Pipe
from time import sleep

def f(conn):
    for _ in range(10):
        conn.send([42, None, 'hello'])
        sleep(2)
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    p.join()
    while True:
    	print (parent_conn.recv())
    print('ext')
