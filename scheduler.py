from typing import List
from queue import PriorityQueue
from concurrent.futures import ThreadPoolExecutor, as_completed


class Scheduler:
    def __init__(self, thread: int):
        self.thread = thread
        self.queue = PriorityQueue()

    def add_task(self, task):
        self.queue.put(task)

    def add_tasks(self, tasks: List):
        for task in tasks:
            self.queue.put(task)

    def run(self):
        futures = []
        with ThreadPoolExecutor(max_workers=self.thread, thread_name_prefix="test") as executor:
            while True:
                _, callback, args = self.queue.get()
                if callback is None:
                    self.queue.task_done()
                    break
                future = executor.submit(callback, args)
                futures.append(future)
                self.queue.task_done()


    def flush(self):
        self.queue.join()
