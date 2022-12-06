import threading
import time
import typing as t

COUNTER = 0

def thread_func(by: int) -> None:
    global COUNTER
    local_counter = COUNTER
    local_counter += by
    time.sleep(0.1)
    
    COUNTER = local_counter
    print(f"{COUNTER=}")

    
if __name__ == '__main__':
    th1 = threading.Thread(target=thread_func, args=(10,),name="Thread 1")
    th2 = threading.Thread(target=thread_func, args=(20,),name="Thread 2")

    th1.start()
    th2.start()
    th1.join()
    th2.join()
    print(COUNTER)