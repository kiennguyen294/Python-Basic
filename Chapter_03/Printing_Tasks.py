import random

from pythonds.basic.queue import Queue


class Printer:
    def __init__(self, ppm):
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task is not None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task is not None:
            return True
        else:
            return False

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate


class Task:
    def __init__(self, time):
        self.time_stamp = time
        self.pages = random.randrange(1, 21)

    def get_stamp(self):
        return self.time_stamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.time_stamp


def simulation(number_second, pages_per_minute):
    lab_printer = Printer(pages_per_minute)
    print_queue = Queue()
    wait_times = []

    for current_second in range(number_second):
        if new_print_task():
            task = Task(current_second)
            print_queue.enqueue(task)

        if (not lab_printer.busy()) and (not print_queue.isEmpty()):
            next_task = print_queue.dequeue()
            wait_times.append(next_task.wait_time(current_second))
            lab_printer.start_next(next_task)

        lab_printer.tick()

    average_wait = sum(wait_times) / len(wait_times)
    print("Average Wait %6.2f secs %3d task remaining." % (average_wait, print_queue.size()))


def new_print_task():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False


for i in range(10):
    simulation(3600, 5)
