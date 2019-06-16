# Evaluate an infix expression and return the result
# Main function is evaluate_expr, with several helper functions
# The process function will do the main job

def evaluate_expr(expr):
    expr = [c for c in expr if c != "'" ]
    print(expr)
    operand_stack = []
    operator_stack = []  # better to use a stack class objects here
    for c in expr:
        print('operator', operator_stack)
        print('operand', operand_stack)
        if c.isdigit():
            operand_stack.append(c)
        elif is_operator(c):
            if operator_stack:
                top_operator_stack = operator_stack[-1]
                if precedence[top_operator_stack] >= precedence[c]:
                    process(operator_stack, operand_stack)
            operator_stack.append(c)

    # process any operators left in the stack
    while len(operator_stack) != 0:
        process(operator_stack,operand_stack)
    return operand_stack[-1]


precedence = {'*': 2,
              '/': 2,
              '+': 1,
              '-': 1
              }


def process(operator_stack, operand_stack):
    num2 = operand_stack.pop()
    num1 = operand_stack.pop()
    print('num1', num1, 'num2',num2)
    operator = operator_stack.pop()
    print(operator)

    # calculate
    result = 0
    if operator == '+':
        result = int(num1) + int(num2)
    elif operator == '-':
        result = int(num1) - int(num2)
    elif operator == '*':
        result = int(num1) * int(num2)
    else:
        result = int(num1) // int(num2)
    operand_stack.append(result)


def is_operand(c):
    if int(c) >= 0 and int(c) <= 9:
        return True
    return False


def is_operator(c):
    if c in ['+', '-', '*', '/']:
        return True
    return False


# Test
expr = '1+2*3-8/4'
print(evaluate_expr(expr))


