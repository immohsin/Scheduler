from task import Task
from scheduler import Scheduler
import threading


def my_name(name):
    print(f"My name is {name} executed by thread {threading.current_thread().name}")


def main():
    thread = 3
    # Create a new scheduler with 3 threads
    scheduler = Scheduler(thread=thread)

    # Create a new task with different priorities
    for i in range(5):
        task = Task(callback=my_name, args=(i,), priority=i).prioritize()
        scheduler.add_task(task)

    # Add the task to the scheduler
    # scheduler.add_tasks([task, task1, task2, task3])
    scheduler.add_task((float("inf"), None, None))

    # Run the scheduler
    scheduler.run()
    scheduler.flush()


if __name__ == '__main__':
    main()
