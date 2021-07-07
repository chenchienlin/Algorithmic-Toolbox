import logging
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def is_word(string, dictionary):
    return string in dictionary

def splitable(S, i, dictionary):
    if i == len(S):
        return True
    for j in range(i, len(S)):
        substr = S[i:j+1]
        if is_word(substr, dictionary):
            LOGGER.debug(f'{substr} {is_word(substr, dictionary)}')
            return splitable(S, j+1, dictionary)

def construct_text_segmentation(S, i, dictionary):
    if i == len(S):
        return []
    for j in range(i, len(S)):
        substr = S[i:j+1]
        if is_word(substr, dictionary):
            LOGGER.debug(f'{substr} {is_word(substr, dictionary)}')
            result = construct_text_segmentation(S, j+1, dictionary)
            if result is not None:
                result.append(substr)
                return result
    return None