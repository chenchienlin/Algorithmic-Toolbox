from week4.parition import partition
import logging
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def quickselect(arr, k):
    lo = 0
    hi = len(arr) - 1
    if k < lo or k > hi: return -1
    while hi >= lo:
        p = partition(arr, lo, hi)
        th = hi - p
        LOGGER.debug(f'Index {p}  Value {arr[p]}  {th}_th largest element')
        if th == k: 
            LOGGER.debug(f'Found {k}_th largest element  Value {arr[th]}')
            return arr[p]
        elif th > k:
            lo = p + 1
        else:
            k = k - th - 1
            hi = p - 1