def valid_paren(st):
    f = []
    for ch in st:
        if ch == '(':
            f.push('(')

        if ch == ')':
            j = f.pop()
            if j is None:
                return False

    return size(f) == 0
