import requests
from datetime import datetime, timezone, timedelta
import bisect

def current_time():
    JST = timezone(timedelta(hours=+9), 'JST')

    now_minute=datetime.now(JST).minute
    freq = [3, 8, 13, 18, 23, 28, 33, 38, 43, 48, 53, 58]
    i = bisect.bisect_left(freq, now_minute)
    if i == 0:
        fetched_time = -1, freq[-1]-1
    else:
        fetched_time = 0, freq[i-1]-1

    preformatted = datetime.now(JST) + timedelta(hours=fetched_time[0])
    current_time = str(preformatted.strftime('%Y%m%d%H')) + str(fetched_time[1]).zfill(2)

    return current_time


def scrape(area, current_time):

    url = 'https://www.jartic.or.jp/d/traffic_info/r1/%s/d/301/%s.json' % (current_time, area)

    r = requests.get(url)

    print('scraper.py: ' + area, current_time)

    if r.status_code == 404:
        return '404 Not Found'

    else:
        return r.json()

