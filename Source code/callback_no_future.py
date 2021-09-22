import threading
import time

def delayed_square_calculator(x, result_callback):
    time.sleep(1)
    result = x * x
    result_callback(result)

def delayed_square(x):
    def call_back(result):
        nonlocal final_result
        final_result = result
    final_result = 0
    calculator = threading.Thread(
        target=delayed_square_calculator, args=(x, call_back)
    )
    calculator.start()
    time.sleep(2)
    return final_result

print(delayed_square(9))
