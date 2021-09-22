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

counters = [
    Count('A', 5, 10),
    Count('B', 6, 15)
]

while counters:
    for counter in counters:
        counter.progress()
        if counter.done:
            counters.remove(counter)
