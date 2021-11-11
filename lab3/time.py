import os
import random
import timeit

'''
with open("text.txt", "a") as file:
    while os.stat("text.txt").st_size < 50e6:
        file.write(str(random.randint(0, 100)) + "\n")
'''

s = """
total = 0
with open("text.txt") as file:
    lines = file.readlines()
    for line in lines:
        if line.strip().isdigit():
            total += int(line.strip())
"""

print(timeit.timeit(s, number=10))

s = """
total = 0
with open("text.txt") as file:
    for line in file:
        if line.strip().isdigit():
            total += int(line.strip())
"""

print(timeit.timeit(s, number=10))

s = """
total = 0
with open("text.txt") as file:
    x = (int(line.strip()) for line in file if line.strip().isdigit())
    total = sum(x)
"""

print(timeit.timeit(s, number=10))
