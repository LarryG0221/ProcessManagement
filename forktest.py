import os
import time

pid=os.fork()

if pid:
    while True:
        print('parent')
        time.sleep(3)

else:
    while True:
        print('child')
        time.sleep(1)

