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
            if splitable(S, j+1, dictionary):
                return True
    return False

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

def construct_all_segmentations(S, i, dictionary):
    if i == len(S):
        return ""
    results = []
    for j in range(i, len(S)):
        substr = S[i:j+1]
        if is_word(substr, dictionary):
            result = construct_all_segmentations(S, j+1, dictionary)
            if isinstance(result, str):
                result = f"{substr}{result}"
                results.append(result)
            elif isinstance(result, list):
                for res in result:
                    res = f"{substr} {res}"
                    results.append(res)
    return results

def count_partition(S, i, dictionary):
    if i == len(S):
        return 1
    count = 0
    for j in range(i+1, len(S)):
        substr = S[i:j+1]
        if is_word(substr, dictionary):
            LOGGER.debug(f'{substr} {is_word(substr, dictionary)}')
            count += count_partition(S, j+1, dictionary)
    return count