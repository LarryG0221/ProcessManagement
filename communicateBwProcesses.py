import multiprocessing
from ctypes import  c_wchar_p

result = []
def square_list(mylist, mylist1):
    print("Result(in process p1): {}".format(result))
    mylist1.value = b'i'
    a = 1
    b= 2
    c = 3
    d = 9
    
if __name__ == "__main__":
    mylist = [1,2,3,4]
    mylist = multiprocessing.Value('c', b'c')
    mylist1 = multiprocessing.Value('c', b'd')
    p1 = multiprocessing.Process(target=square_list, args=(mylist, mylist1))
    p1.start()
    p1.join()
    print("Result(in main program): {}".format(mylist1.value.decode('ascii')))

    str1='123'
    
