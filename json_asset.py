import requests
from datetime import datetime, timezone, timedelta

def current_time():
    JST = timezone(timedelta(hours=+9), 'JST')

    frequency = [3, 8, 13, 18, 23, 28, 33, 38, 43, 48, 53, 58]
    now_minute = datetime.now(JST).minute

    for i, minute in enumerate(frequency):
        if now_minute in [0, 1, 2, 3]:
            preformatted = datetime.now(JST) + timedelta(minutes=-5)
            current_time = str(preformatted.strftime('%Y%m%d%H')) + str(frequency[-1]-1).zfill(2)
            break
        elif now_minute in [58, 59]:
            current_time = str(datetime.now(JST).strftime('%Y%m%d%H')) + str(frequency[-1]-1).zfill(2)
            break
        elif now_minute > minute: #3:12
            continue
        else:
            if now_minute > frequency[i-1]:
                current_time = str(datetime.now(JST).strftime('%Y%m%d%H')) + str(frequency[i-1]-1).zfill(2)
                break

    return current_time

def scrape(area, current_time=current_time()):

    url = 'https://www.jartic.or.jp/d/traffic_info/r1/%s/d/301/%s.json' % current_time, area

    r = requests.get(url)

    if r.status_code == 404:
        return '404 Not Found'

    else:
        return r.json()

