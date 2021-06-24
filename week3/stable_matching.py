import logging
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()


def stable_matching(intern_list, hospital_list):
    n_col = len(intern_list[0])
    int_choices = [None for i in range(0, n_col)]
    hsp_choices = [None for i in range(0, n_col)]
    Q = list()
    match_count = 0
    round = 0
    records = list()
    while match_count < n_col or round < n_col:
        LOGGER.info(f'==================== Round {round} ====================')
        Q = [i for i in range(0, n_col)]
        round_match = [False for i in range(0, n_col)]
        while len(Q) > 0:
            hsp_idx = Q.pop(0)
            if hsp_choices[hsp_idx] == None: # unmatched hospital makes offer
                int_idx = hospital_list[hsp_idx][round]
                round_match[hsp_idx] = True # mark the hospital already makes their offer in this round
                LOGGER.debug(round_match)
                # LOGGER.debug(f'{hsp_idx}_th hospital makes an offer to {int_idx}_th intern')
                if int_choices[int_idx] == None:
                    LOGGER.debug(f'{int_idx}_th intern does not have offer yet. {int_idx}_th intern accepts {hsp_idx}_th hospital')
                    hsp_choices[hsp_idx] = int_idx
                    int_choices[int_idx] = hsp_idx
                    match_count += 1
                    records.append(hsp_choices.copy())
                else:
                    prev_hsp_idx = int_choices[int_idx]
                    prev = preference(intern_list, int_idx, prev_hsp_idx)
                    new = preference(intern_list, int_idx, hsp_idx)
                    if new < prev:
                        LOGGER.debug(f'{int_idx}_th intern rejects previous offer from {prev_hsp_idx}_th hospital accepts {hsp_idx}_th hospital')
                        hsp_choices[prev_hsp_idx] = None
                        hsp_choices[hsp_idx] = int_idx
                        int_choices[int_idx] = hsp_idx
                        
                        if round_match[prev_hsp_idx] != True: # if prev_hsp_idx haven't make their offer in the round
                            Q.append(prev_hsp_idx)
                        
                        records.append(hsp_choices.copy())
                    else:
                        LOGGER.debug(f'{int_idx}_th intern keeps previous offer from {prev_hsp_idx}_th hospital rejects {hsp_idx}_th hospital')
                        records.append(hsp_choices.copy())
        round += 1
    return int_choices, hsp_choices, records

def preference(intern_list, intern_idx, hospital_idx):
    p = -1
    pref = intern_list[intern_idx]
    for i in range(0, len(pref)):
        if pref[i] == hospital_idx:
            p = i
            break
    if p < 0:
        raise KeyError
    else:
        return p