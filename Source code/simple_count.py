import time

class Count:
    def __init__(self, name, start, finish):
        self.name = name
        self.value = start
        self.finish = finish
        self.done = False

    def progress(self):
        if self.value > self.finish:
            self.done = True
            return
        print(self.name, self.value)
        self.value += 1
        time.sleep(0.5)
