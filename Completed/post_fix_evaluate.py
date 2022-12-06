# equation PEMDAS 
def postfix_evaluate(items):
    result = []
    for a in items:
        if type(a) is int:
            result.append(a)
            continue

        op1 = result.pop()
        op2 = result.pop()

        if a == '+':
            result.append(op2 + op1)
        elif a == '-':
            result.append(op2 - op1)
        elif a == '*':
            result.append(op2 * op1)
        elif a == '/':
            if op1!=0:
                result.append(op2 // op1)
            else:
                result.append(0)
    return result.pop()