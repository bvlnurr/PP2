import math
import time

def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000.0)
    result = math.sqrt(number)
    print(f"Square root of {number} after {delay_ms} milliseconds is {result}")

delayed_sqrt(25, 2123)