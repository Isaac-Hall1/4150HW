import sys
from time import sleep

def process_input():
    # Read the first line: number of values and total time
    first_line = input().split()
    num_values = int(first_line[0])  # Number of values
    total_time = int(first_line[1])  # Total time
    
    left_values = []
    right_values = []

    # Read the subsequent lines for left and right values
    for _ in range(num_values):
        line = input().split()
        left_values.append(int(line[0]))
        right_values.append(int(line[1]))

    return num_values, total_time, left_values, right_values

def checkConstant(mid):
    sum_result = 0
    for index, val in enumerate(left_values):
        if (mid + right_values[index]) != 0:
            sum_result += val / (mid + right_values[index])  
        else:
            return None
    return sum_result

def BinarySearch(target):
    low, upper = max(0.01 - r for r in right_values), 1e7 
    precision = 1e-9
    while low <= upper:
        mid = (low + upper) / 2
        checkMid = checkConstant(mid)
        print(checkMid)
        if checkMid is None:
            low += precision
            continue
        if abs(checkMid - target) < precision:
            return mid
        elif checkMid < target:
            upper = mid
        else:
            low = mid
    return -1

num_values, total_time, left_values, right_values = process_input()
print(BinarySearch(total_time))