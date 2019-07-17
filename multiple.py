# Speed calculated based on multiple attempts.

from utils import calc_mean as mean
import requests
import sys
import time


# Max requests to make to the requested URL
ATTEMPTS = 5

# Seconds to delay after each request
DELAY_TIME = 2


try:
    url = sys.argv[1]
except IndexError:
    url = 'https://github.com'
    print("No URL specified. Using default 'https://github.com'.\n")


def timed(func):
    stats = {}
    for _ in range(ATTEMPTS):
        start = time.time()
        size = func()
        duration = time.time() - start
        print("Request sent. Remaining %d" %(ATTEMPTS - _))
        stats[size] = duration
        time.sleep(DELAY_TIME)

    """
    APPROACH 1
    ==================================================
    Find speed by dividing mean of all `size`s and `duration`s.
    Result is dependent on the size of the `stats` dict.

    APPROACH 2
    ==================================================
    Find speed by dividing sum of all `size`s and `duration`s.
    Result is size-independent.

    """

    # Using first approach...
    speed_bps = mean.use_mean(stats)

    # # Using second approach...
    # speed_bps = mean.use_sum(stats)

    print("Speed:   {:.2f} kbps".format(speed_bps / 1000))


@timed
def make_timed_request():
    resp = requests.get(url)
    size = len(resp.content)
    return size


if __name__ == "__main__":
    make_timed_request
