<<<<<<< HEAD
import sys

max_weight = None

try:
    capacity = int(sys.argv[1])
    weights = sys.argv[2::]
    w = [1] + capacity * [0]

    for i in range(len(weights)):
        for j in range(capacity, int(weights[i]) - 1, -1):
            if w[j - int(weights[i])] == 1:
                w[j] = 1
    i = capacity
    while w[i] == 0:
        i -= 1
    max_weight = i

except ValueError:
    print("Values must be integers")

print(max_weight)
=======
import sys

capacity = int(sys.argv[1])
weights = sys.argv[2::]

def knapsack(capacity, weights):
    w = [1] + capacity * [0]

    for i in range(len(weights)):
        for j in range(capacity, int(weights[i]) - 1, -1):
            if w[j - int(weights[i])] == 1:
                w[j] = 1
    i = capacity
    while w[i] == 0:
        i -= 1
    return i

print(knapsack(capacity, weights))
>>>>>>> eaaea3fc7e188c1b42e6d74ec6ea27892fb2a0b1
