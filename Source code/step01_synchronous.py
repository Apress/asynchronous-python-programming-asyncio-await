import time

def count(name, start, finish):
    for i in range(start, finish):
        print(name, i)
        time.sleep(0.5)

count('A', 5, 10)
count('B', 6, 20)
