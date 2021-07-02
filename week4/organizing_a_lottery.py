import math
import logging
from week4.number_of_inversions import LOGGER
logging.basicConfig(level=logging.DEBUG)

def organizing_a_lottery_naive(segs, points):
    b = []
    for p in points:
        in_range = int(check_in_a_range(p, segs))
        b.append(in_range)
    return b

def check_in_a_range(p, segs):
    in_range = 0
    for seg in segs:
        head = seg[0]
        tail = seg[1]
        if p >= head and p <= tail:
            in_range += 1
    return in_range

def organizing_a_lottery(segs, points):
    idxs = [i for i in range(len(points))]
    zipped_lists = zip(points, idxs)
    sorted_zipped_lists = sorted(zipped_lists)
    sorted_lists = [list(tup) for tup in zip(*sorted_zipped_lists)]
    points = sorted_lists[0]
    idxs = sorted_lists[1]
    counts = [0 for _ in range(len(points))]
    
    for seg in segs:
        start, end = seg[0], seg[1]
        
        first_idx = find_greater(points, start)
        last_idx = find_smaller(points, end)
        if first_idx != -1 and last_idx != -1:
            for idx in range(first_idx, last_idx+1):
                origin_idx = idxs[idx]
                counts[origin_idx] += 1
    return counts

def find_greater(arr, target):
    lo = 0
    hi = len(arr) - 1
    while hi >= lo:
        mid = int(math.floor( (lo+hi)/2 ))
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1
    # Out of while loop, lo > hi
    if lo <= len(arr) - 1:
        return lo
    else:
        LOGGER.info('Out of range')
        return -1

def find_smaller(arr, target):
    lo = 0
    hi = len(arr) - 1
    while hi >= lo:
        mid = int(math.floor( (lo+hi)/2 ))
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1
    # Out of while loop, lo > hi
    if hi >= 0:
        return hi
    else:
        LOGGER.info('Out of range')
        return -1