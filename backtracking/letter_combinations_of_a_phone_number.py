def letter_combinations(digits):
    D = dict()
    frt_chr = 97
    for i in range(2, 7):
        D[str(i)] = [chr(j+frt_chr) for j in range(3)]
        frt_chr += 3
    D["7"] = ["p","q","r","s"]
    D["8"] = ["t","u","v"]
    D["9"] = ["w","x","y","z"]
    return recur_letter_combinations(digits, D, 0)

def recur_letter_combinations(digits, D, i):
    if i == len(digits):
        return ""
    else:
        results = []
        for letter in D[digits[i]]:
            res = recur_letter_combinations(digits, D, i+1)
            if isinstance(res, str):
                res += letter
                results.append(res)
            else:
                for l in res:
                    l += letter
                    results.append(l)
        return results