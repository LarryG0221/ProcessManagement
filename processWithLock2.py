# Python program to illustrate 
# the concept of race condition 
# in multiprocessing 
import multiprocessing 
from multiprocessing import  Lock

# function to withdraw from account 
def withdraw(lock, balance):
    lock.acquire()

    for _ in range(10000):
	    balance.value = balance.value - 1
    lock.release()

# function to deposit to account 
def deposit(lock, balance):
    lock.acquire()
    for _ in range(100):
        balance.value = balance.value + 1
    lock.release()

def perform_transactions(lock): 

	# initial balance (in shared memory) 
	balance = multiprocessing.Value('i',14)

	# creating new processes 
	p1 = multiprocessing.Process(target=withdraw, args=(lock, balance,)) 
	p2 = multiprocessing.Process(target=deposit, args=(lock, balance,)) 

	# starting processes 
	p1.start() 
	p2.start() 

	# wait until processes are finished 
	p1.join() 
	p2.join() 

	# print final balance 
	print("Final balance = {}".format(balance.value)) 

if __name__ == "__main__":
    lock = Lock()
    for _ in range(10): 

        # perform same transaction process 10 times 
        perform_transactions(lock) 
