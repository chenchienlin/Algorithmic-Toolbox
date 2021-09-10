def generate_parentheses(n, i, j):
    if i == n and j == n:
        return ""
    else:
        results = []
        if i < n:
            a = generate_parentheses(n, i+1, j)
            if isinstance(a, str):
                a = f"({a}"
                results.append(a)
            elif isinstance(a, list):
                for elem in a:
                    elem = f"({elem}"
                    results.append(elem)
        if j < i:
            b = generate_parentheses(n, i, j+1)
            if isinstance(b, str):
                b = f"){b}"
                results.append(b)
            elif isinstance(b, list):
                for elem in b:
                    elem = f"){elem}"
                    results.append(elem)
        return results