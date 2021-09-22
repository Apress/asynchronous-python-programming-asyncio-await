import time

class Scheduler:
    def __init__(self):
        self.active_tasks = []
        self.delayed_tasks = []

    def submit_soon(self, task):
        self.active_tasks.append(task)

    def process_active_tasks(self):
        active_tasks = self.active_tasks.copy()
        self.active_tasks = []
        for task in active_tasks:
            task.progress()

    # check_delayed_tasks and wait_for_next_delayed_task
    # shown on next screen

    def start(self):
        while self.active_tasks + self.delayed_tasks:
            # self.check_delayed_tasks()
            if self.active_tasks:
                self.process_active_tasks()
            # else:
                # self.wait_for_next_delayed_task()

scheduler = Scheduler()
