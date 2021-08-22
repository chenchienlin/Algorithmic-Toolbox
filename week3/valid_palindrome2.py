def valid_palindrome2(s):
    i = 0
    j = len(s) - 1
    while i <= j:
        if s[i] != s[j]:
            return is_valid(s, i+1, j) or is_valid(s, i, j-1)
        i += 1
        j -= 1
    return True

def is_valid(s, i, j):
    while i <= j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True