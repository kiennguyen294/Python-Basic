import random
import threading
import time
import _thread


def worker(name: str) -> None:
    print(f'Started worker {name}')
    worker_time = random.choice(range(1, 5))
    time.sleep(worker_time)
    print(f'{name} worker finished in {worker_time} seconds')


# def _counter(counter, thread_name):
#     while counter:
#         time.sleep(0.01)
#         print("{}: {}".format(thread_name, counter))
#         counter -= 1
#
#
# counter = 5
#
# try:
#     _thread.start_new_thread(_counter(counter, "thread no 1"))
#     print("\n")
#     _thread.start_new_thread(_counter(counter, "thread no 2"))
#
# except:
#     print("Error: unable to start thread")
#
# while counter:
#     counter -= 1
#     pass

if __name__ == '__main__':
    for i in range(5):
        thread = threading.Thread(target=worker, args=(f'computer_{i}',), )
        thread.start()
