import threading
import typing as t

def thread_func() -> None:
    print(f"Hello from {threading.current_thread().getName()}")

if __name__ == '__main__':
    th1 = threading.Thread(target=thread_func, args=(),name="Thread 1")
    th2 = threading.Thread(target=thread_func, args=(),name="Thread 2")

    th1.start()
    th2.start()
    th1.join()
    th2.join()