import time


class SynchronousCounter:
    def __init__(self, number):
        self.number = number
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.number == self.current:
            raise StopIteration
        time.sleep(1)
        return self.current


def main():
    for i in SynchronousCounter(5):
        print(i)

main()
