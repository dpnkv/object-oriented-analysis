import sys

expression = ""
result = None
for i in range(1, len(sys.argv)):
    expression += sys.argv[i]

try:
    result = eval(expression)
except ZeroDivisionError:
    print("Division by zero!")
except (NameError, TypeError, ValueError, SyntaxError):
    print("Invalid expression!")

print("Result:", result)
