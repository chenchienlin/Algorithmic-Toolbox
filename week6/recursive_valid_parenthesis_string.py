def recursive_valid_parenthesis_string(s, i, count):
    if i == len(s):
        return True if count == 0 else False
    elif s[i] == "(":
        return recursive_valid_parenthesis_string(s, i+1, count+1)
    elif s[i] == ")":
        return recursive_valid_parenthesis_string(s, i+1, count-1)
    else:
        assert s[i] == "*"
        a = recursive_valid_parenthesis_string(s, i+1, count)
        b = recursive_valid_parenthesis_string(s, i+1, count+1)
        c = recursive_valid_parenthesis_string(s, i+1, count-1)
        return a or b or c