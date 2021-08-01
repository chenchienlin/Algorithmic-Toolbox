def recursive_wildcard_pattern_matching(string, pattern, i, j):
    if i == len(string) or j == len(pattern):
        if i == len(string) and j == len(pattern):
            return True
        else:
            return False
    elif string[i] == pattern[j] or pattern[j] == '?':
        return True and recursive_wildcard_pattern_matching(string, pattern, i+1, j+1)
    else:
        return False

def recursive_wildcard_pattern_matching2(string, pattern, i, j):
    if i == len(string) or j == len(pattern):
        if i == len(string) and j == len(pattern):
            return True
        else:
            return False
    elif string[i] == pattern[j] or pattern[j] == '?':
        return True and recursive_wildcard_pattern_matching2(string, pattern, i+1, j+1)
    elif pattern[j] == '*':
        a = True and recursive_wildcard_pattern_matching2(string, pattern, i+1, j)
        b = True and recursive_wildcard_pattern_matching2(string, pattern, i, j+1)
        c = True and recursive_wildcard_pattern_matching2(string, pattern, i+1, j+1)
        return a or b or c
    else:
        return False

string = "baaabab"
# pattern = "ba*a?"
pattern = "*****ba*****ab"
# pattern = "a*ab"
print(recursive_wildcard_pattern_matching2(string, pattern, i=0, j=0))