<<<<<<< HEAD
import sys

result = None

try:
    operand_1 = int(sys.argv[2])
    operand_2 = int(sys.argv[3])

    if (sys.argv[1] == "add"):
        result = operand_1 + operand_2
    elif (sys.argv[1] == "sub"):
        result = operand_1 - operand_2
    elif (sys.argv[1] == "mul"):
        result = operand_1 * operand_2
    elif (sys.argv[1] == "div"):
        result = operand_1 / operand_2
    else: print("Invalid operator!")

except ZeroDivisionError:
    print("Division by zero!")
except IndexError:
    print("Invalid number of arguments!")
except ValueError:
    print("Invalid input!")

print("Result:", result)
=======
import sys

operand_1 = int(sys.argv[2])
operand_2 = int(sys.argv[3])

if (sys.argv[1] == "add"):
    answer = operand_1 + operand_2
elif (sys.argv[1] == "sub"):
    answer = operand_1 - operand_2
elif (sys.argv[1] == "mul"):
    answer = operand_1 * operand_2
elif (sys.argv[1] == "div"):
    answer = operand_1 / operand_2

print(answer)
>>>>>>> eaaea3fc7e188c1b42e6d74ec6ea27892fb2a0b1
