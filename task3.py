def get_terms(expr):
    terms = []
    tmp = ""
    for term in expr + ' ':
        if term.isnumeric():
            tmp += term
        elif term == ' ':
            terms.append(tmp)
            break
        else:
            terms.append(tmp)
            terms.append(term)
            tmp = ""
    return terms


def calculate(expr):
    terms = get_terms(expr)
    n1 = terms[0]
    n2 = terms[2]
    operator = terms[1]
    if operator == '#':
        return int(n2) % int(n1)
    elif operator == '!':
        sum1 = 0
        sum2 = 0
        for t in n1:
            sum1 += int(t)
        for t in n2:
            sum2 += int(t)
        return n2 if sum1 < sum2 else n1
    elif operator == '@':
        return n2 if int(n1) < int(n2) else n1
    elif operator == '$':
        return n2 if len(n1) < len(n2) else n1


if __name__ == '__main__':
    expresion = input("Please enter expresion: ")
    print(calculate(expresion))
