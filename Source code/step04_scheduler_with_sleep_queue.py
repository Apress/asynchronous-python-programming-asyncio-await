import count
from scheduler import scheduler
import time

scheduler.submit_soon(count.Count('A', start=5, finish=10, delay=0.7))
scheduler.submit_soon(count.Count('B', start=6, finish=20, delay=0.3))
scheduler.submit_soon(count.Count('C', start=100, finish=105))

start_time = time.time()
scheduler.start()
print(f'{time.time() - start_time:.3} seconds lapsed')
