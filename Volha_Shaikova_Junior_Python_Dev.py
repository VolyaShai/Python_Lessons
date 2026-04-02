from decimal import Decimal
import numpy as np

def task_1(str_1, str_2):
    start, end = min(str_1, str_2), max(str_1, str_2)
    return [f"{i:05}"[:2] + "-" + f"{i:05}"[2:]
           for i in range(int(start.replace("-", "")), int(end.replace("-", "")) + 1)]


def task_2(test_range, n):
    control_range = list(range(1, n+1))
    missing_range = [x for x in control_range if x not in test_range]
    return missing_range


def task_3():
    decimal_list = list(Decimal(x) for x in (np.arange(2, 5.5, 0.5)))
    return decimal_list
    # Return will look like a list of numbers, but the type will not be Decimal
    # return float_list= list(float(x) for x in decimal_list)
