import logging
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def is_word(string, dictionary):
    return string in dictionary

def dp_splitable(S, i, dictionary, memo):
    if i == len(S):
        return True
    for j in range(i, len(S)):
        substr = S[i:j+1]
        if is_word(substr, dictionary):
            LOGGER.debug(f'{substr} {is_word(substr, dictionary)}')
            if j+1 in memo and memo[j+1] is True:
                return True
            else:
                memo[j+1] = dp_splitable(S, j+1, dictionary, memo)
                if memo[j+1] is True:
                    return True
    return False