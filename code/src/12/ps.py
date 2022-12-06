import multiprocessing
import typing as t

COUNTER = 1

def process_func() -> None:
    global COUNTER
    COUNTER += 1
    print(f"{COUNTER=} in process {multiprocessing.current_process().name}")

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=process_func, name="Process 1")
    p2 = multiprocessing.Process(target=process_func, name="Process 2")

    p1.start()
    p2.start()

    p1.join()
    p2.join()
