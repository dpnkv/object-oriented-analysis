import sys

expr = ""
for i in range(1, len(sys.argv)):
    expr += sys.argv[i]

print(eval(expr))
