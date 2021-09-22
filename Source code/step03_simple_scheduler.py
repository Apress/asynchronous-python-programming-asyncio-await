import simple_count

class SimpleScheduler:
    def __init__(self):
        self.active_tasks = []

    def submit(self, task):
        self.active_tasks.append(task)

    def start(self):
        while self.active_tasks:
            tasks = self.active_tasks
            self.active_tasks = []
            for task in tasks:
                task.progress()
                if not task.done:
                    self.submit(task)

scheduler = SimpleScheduler()
scheduler.submit(simple_count.Count('A', 5, 10))
scheduler.submit(simple_count.Count('B', 6, 15))
scheduler.start()
