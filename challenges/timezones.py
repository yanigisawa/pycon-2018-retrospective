# Open the attached file. Every line contains a series of keys and values. Build a histogram of the time zones and
# identify the time zone that shows up most frequently with a user-agent string that includes ipad (search for all
# variations of case in the term ipad (i.e. IPAD,iPad, etc)).
#
# For example, if you counted the time zones:
#
# Europe/Bratislava 8
# America/Los_Angeles 4
# America/Chihuahua 3
# For your answer, you would enter the number 8.

import json
import time

with open('usa.gov.json') as f:
    zones = {}
    for line in f:
        req = json.loads(line)
        if 'a' not in req.keys():
            continue
        agent = req['a'].lower()
        if 'ipad' in agent:
            if req['tz'] not in zones.keys():
                zones[req['tz']] = 0
            zones[req['tz']] += 1

    print(zones)
    most = 0
    for key in zones.keys():
        if not key:
            continue
        if zones[key] > most:
            most = zones[key]

    print(most)
