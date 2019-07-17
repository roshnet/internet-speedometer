# Speed calculated based on single attempt.

import requests
import sys
import time

try:
    url = sys.argv[1]
except IndexError:
    url = 'https://github.com'
    print("No URL specified. Using default 'https://github.com'.\n")


def timed(func):
    start = time.time()
    size_byte = func()
    duration_sec = time.time() - start
    speed_bps = size_byte / duration_sec
    print("Time taken:    {:.2f} ms".format(duration_sec * 1000))
    print("Speed:         {:.2f} kbps".format(speed_bps / 1000))


@timed
def make_timed_request():
    resp = requests.get(url)
    size = len(resp.content)
    return size


if __name__ == "__main__":
    make_timed_request
