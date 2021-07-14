def recursive_edit_distance(str1, str2, leni, lenj):
    if leni == 0:
        return lenj
    elif lenj == 0:
        return leni
    elif str1[leni-1] == str2[lenj-1]:
        return 0 + recursive_edit_distance(str1, str2, leni-1, lenj-1)
    else:
        a = 1 + recursive_edit_distance(str1, str2, leni-1, lenj-1)
        b = 1 + recursive_edit_distance(str1, str2, leni-1, lenj)
        c = 1 + recursive_edit_distance(str1, str2, leni, lenj-1)
        return min(a, b, c)