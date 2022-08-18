'''
An experimental script to figure out the maximum call stack depth in Python.
'''

depth = 0

def recursive():
    global depth
    depth += 1
    recursive()

try:
    recursive()
except RecursionError:
    print(f"Got {depth} calls deep before a RecursionError was raised!")
    # 2022-08-17 run: depth == 999
