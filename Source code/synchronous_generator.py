import time


def synchronous_counter(number):
    for i in range(1, number):
        yield i
        time.sleep(1)


def main():
    for i in synchronous_counter(5):
        print(i)

main()
