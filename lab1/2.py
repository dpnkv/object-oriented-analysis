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
