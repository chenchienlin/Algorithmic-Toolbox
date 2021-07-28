import logging
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def all_possible_strings(s, k, ans):
    if k == 0:
        LOGGER.info(ans)
        return
    for elem in s:
        ans[k-1] = elem
        all_possible_strings(s, k-1, ans)

def construct_all_possible_strings(s, k):
    if k == 0:
        return ['']
    results = []
    for elem in s:
        res = construct_all_possible_strings(s, k-1)
        for i in range(len(res)):
            res[i] = f'{res[i]}{elem}'
            results.append(res[0])
    return results