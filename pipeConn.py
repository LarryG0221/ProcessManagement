from multiprocessing import Process, Pipe
from time import sleep

def f(conn):
    while True:
        conn.send([42, None, 'hello'])
        sleep(2)
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    while True:
        print(parent_conn.recv())
        print(1)
