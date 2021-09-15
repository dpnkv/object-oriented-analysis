import sys

formula = sys.argv[1]
sign = ['+', '-']

is_formula_valid = True
answer = None
length = len(formula)
is_prev_num = True

if length == 0 or (length == 1 and not formula[0].isdigit() or
                   not formula[length - 1].isdigit()):
    is_formula_valid = False
else:
    for char in formula:
        if not char.isdigit() and not char in sign or\
        not is_prev_num and char in sign:
            is_formula_valid = False
            break
        is_prev_num = char.isdigit()

if is_formula_valid:
    answer = eval(formula)

print(f"({is_formula_valid}, {answer})")
