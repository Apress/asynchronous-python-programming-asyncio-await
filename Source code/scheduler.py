import time

class Scheduler:
    def __init__(self):
        self.active_tasks = []
        self.delayed_tasks = []

    def submit_soon(self, task):
        self.active_tasks.append(task)

    def submit_later(self, task, delay):
        start_time = time.time() + delay
        self.delayed_tasks.append((start_time, task))
        self.delayed_tasks.sort()

    def check_delayed_tasks(self):
        now = time.time()
        still_delayed = []
        for start_time, task in self.delayed_tasks:
            if start_time <= now:
                self.submit_soon(task)
            else:
                still_delayed.append((start_time, task))
        self.delayed_tasks = still_delayed

    def process_active_tasks(self):
        active_tasks = self.active_tasks.copy()
        self.active_tasks = []
        for task in active_tasks:
            task.progress()

    def wait_for_next_delayed_task(self):
        if not self.delayed_tasks:
            return
        time.sleep(self.delayed_tasks[0][0] - time.time())

    def start(self):
        while self.active_tasks + self.delayed_tasks:
            self.check_delayed_tasks()
            if self.active_tasks:
                self.process_active_tasks()
            else:
                self.wait_for_next_delayed_task()

scheduler = Scheduler()
