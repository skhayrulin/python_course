import threading
import time

COUNT = 50000000

def countdown(n):
    while n > 0:
        n -= 1

if __name__ == '__main__':
    start = time.time()
    countdown(COUNT)
    end = time.time()
    print(f"single thread time {end - start}")
    
    th1 = threading.Thread(target=countdown, args=(COUNT//2,))
    th2 = threading.Thread(target=countdown, args=(COUNT//2,))
    start = time.time()
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    end = time.time()
    print(f"two thread time {end - start}")