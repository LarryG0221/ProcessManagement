import signal
import time
import os
import threading

def sighandler(signum, frame):
    print('receviing a signal ',signum)

    return


def rec():
    print('receiving ', signal.getsignal())

    signal.alarm(2)

def send():

    print('sending')
    signal.al

time.sleep(4)
signal.alarm(2)




print('ending')
time.sleep(4)
