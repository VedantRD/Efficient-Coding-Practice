# Simplify the given algebraic expression consisting of  ‘+’, ‘-‘ operators and parentheses.
# input  => a-(b+c)
# output => a-b-c


def solve_expression(exp):
    res = ''
    stack = [0]
    n = len(exp)
    i = 0
    while i < n:
        if exp[i] == '+':
            if stack[-1] == 1:
                res += '-'
            else:
                res += '+'
        elif exp[i] == '-':
            if stack[-1] == 1:
                res += '+'
            else:
                res += '-'
        elif exp[i] == '(':
            if exp[i-1] == '-':
                if stack[-1] == 1:
                    stack.append(0)
                else:
                    stack.append(1)
            else:
                stack.append(stack[-1])
        elif exp[i] == ')':
            stack.pop()
        else:
            res += exp[i]
        i += 1
    return res


exp1 = 'a-(b+c)'
exp2 = 'a-(b-c-(d+e))-f'
print(solve_expression(exp1))
print(solve_expression(exp2))
