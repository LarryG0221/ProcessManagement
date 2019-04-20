from multiprocessing import Pipe, Process
import time

def fun1(i):
	time.sleep(2)
	print('string%s'% i)


def main():
	p = Process(target=fun1, args=(2,),daemon=True)
	p.start()
	p.join()
	print('next')
	time.sleep(2)

main()

