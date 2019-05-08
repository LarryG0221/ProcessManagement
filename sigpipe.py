import os
import sys
import signal
import time
import pprint

def recSign(signum, frame):
    print('revice a signal %s'%signum)

    return


def reponseSIG():

    signal.signal(signal.SIGTERM, recSign)
    signal.signal(signal.SIGHUP, recSign)

    pid = os.getpid()

    while True:
        print('waiting', pid)
        time.sleep(3)

def recvsignal(signum, frame):
    print('receiving.... ', signum)
    raise SystemExit('exit')
    return 

def responseSIGS():

    signal.signal(signal.SIGHUP, recvsignal)
    signal.signal(signal.SIGINT, signal.SIG_IGN)

    print('pid -- ', os.getpid())
    signal.pause()
    
def signalHandler(signum, frame):

    print('receviing.... ', signum)
    return

def respSignals():

    signal.signal(signal.SIGTERM,signalHandler)
    signal.signal(signal.SIGHUP,signal.SIG_IGN)

    print('waiting in pid -- ', os.getpid())

    signal.pause()


def getsign():

    signal.signal(signal.SIGUSR1, signalHandler)
    signal.signal(signal.SIGUSR2, signalHandler)

    print ('My PID is:', os.getpid())

    signalsnames={}
    for i in dir(signal):
        if i.startswith('SIG') and not i.startswith('SIG_'):
            signalsnames[getattr(signal,i)] = i


    for s,name in signalsnames.items():
        handler = signal.getsignal(s)
        if handler is signal.SIG_DFL:
            handler='dfl'
        if handler  == signal.SIG_IGN:
            handler='ign'
        print((name,s), handler)
        
def sigAlrm():
    signal.signal(signal.SIGALRM, recSign)
    signal.alarm(3)

    print('before')
    for i in range(4):
        time.sleep(1)
        print('1 sec')
    print('after')


def ignoreSIG():
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    signal.signal(signal.SIGUSR1, recvsignal)

    print('000pid is ',os.getpid())
    signal.pause()

ignoreSIG()
