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
