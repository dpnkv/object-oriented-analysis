<<<<<<< HEAD
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
=======
import sys

expr = ""
for i in range(1, len(sys.argv)):
    expr += sys.argv[i]

print(eval(expr))
>>>>>>> eaaea3fc7e188c1b42e6d74ec6ea27892fb2a0b1
