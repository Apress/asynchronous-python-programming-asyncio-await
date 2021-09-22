from scheduler import scheduler

class Count:
    def __init__(self, name, start, finish, delay=0):
        self.name = name
        self.value = start
        self.finish = finish
        self.delay = delay

    def progress(self):
        if self.value > self.finish:
            return
        print(self.name, self.value)
        self.value += 1
        if self.delay:
            scheduler.submit_later(self, self.delay)
        else:
            scheduler.submit_soon(self)
