import requests
from datetime import datetime, timezone, timedelta
import bisect

def current_time():
    JST = timezone(timedelta(hours=+9), 'JST')

    def helper(now_minute=datetime.now(JST).minute):
        freq = [3, 8, 13, 18, 23, 28, 33, 38, 43, 48, 53, 58]
        i = bisect.bisect_left(freq, now_minute)
        if i == 0:
            return -1, freq[-1]-1
        else:
            return 0, freq[i-1]-1

    preformatted = datetime.now(JST) + timedelta(hours=helper()[0])
    current_time = str(preformatted.strftime('%Y%m%d%H')) + str(helper()[1]).zfill(2)

    return current_time


def scrape(area, current_time=current_time()):

    url = 'https://www.jartic.or.jp/d/traffic_info/r1/%s/d/301/%s.json' % current_time, area

    r = requests.get(url)

    if r.status_code == 404:
        return '404 Not Found'

    else:
        return r.json()

