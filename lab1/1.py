import sys

exp = sys.argv
exp.pop(0)

expr = ""
for i in range(0, len(sys.argv)):
    expr += sys.argv[i]

print(eval(expr))
