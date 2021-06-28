import logging 
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()

def tower_of_hanoi(n, src, dist, temp):
    if n > 0:
        tower_of_hanoi(n-1, src, temp, dist)
        LOGGER.info(f'Moved disk {n} from {src} to {dist}')
        tower_of_hanoi(n-1, temp, dist, src)

tower_of_hanoi(n=3, src='A', dist='C', temp='B')