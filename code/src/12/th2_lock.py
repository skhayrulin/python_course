import threading
import time
import typing as t

COUNTER = 0

def thread_func(by: int, l: threading.Lock) -> None:
    global COUNTER
    l.acquire()
    local_counter = COUNTER
    local_counter += by
    time.sleep(0.1)
    

    COUNTER = local_counter
    print(f"{COUNTER=}")
    l.release()

    
if __name__ == '__main__':
    lock = threading.Lock()
    th1 = threading.Thread(target=thread_func, args=(10,lock),name="Thread 1")
    th2 = threading.Thread(target=thread_func, args=(20,lock),name="Thread 2")

    th1.start()
    th2.start()
    th1.join()
    th2.join()
    print(COUNTER)