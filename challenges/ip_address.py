# In the attached list of IP addresses, what country has the most IPs? The answer should be the two-letter
# country code of the country. If multiple countries have the same amount, use the country which comes last in alphabetical order.
#
# For
import requests

with open('intl_ip_list.txt') as f:
    countries = {}
    for line in f:
        ip = line.strip()
        url = f'https://www.iplocate.io/api/lookup/{ip}'
        resp = requests.get(url)
        resp_json = resp.json()
        if resp_json['country_code'] not in countries.keys():
            countries[resp_json['country_code']] = 0
        countries[resp_json['country_code']] += 1

    s = [(key, countries[key]) for key in sorted(countries, key=countries.get, reverse=True)]
    print(s)


# bc:5f:f4:68:55:81
# 20:0c:c8:d5:d6:80
# 20:0c:c8:d5:d6:80
# bc:5f:f4:68:55:81
# Ethernet II, Src: Raspberr_54:60:65 (b8:27:eb:54:60:65), Dst: Broadcast (ff:ff:ff:ff:ff:ff)
# Ethernet II, Src: AsrockIn_68:55:81 (bc:5f:f4:68:55:81), Dst: IPv4mcast_7f:ff:fa (01:00:5e:7f:ff:fa)
# Ethernet II, Src: Netgear_d5:d6:80 (20:0c:c8:d5:d6:80), Dst: c6:cc:f4:6d:94:6e (c6:cc:f4:6d:94:6e)
# Ethernet II, Src: AsrockIn_68:55:81 (bc:5f:f4:68:55:81), Dst: IPv6mcast_0c (33:33:00:00:00:0c)
# Ethernet II, Src: Netgear_d5:d6:80 (20:0c:c8:d5:d6:80), Dst: bc:72:f4:68:69:61 (bc:72:f4:68:69:61)
# Ethernet II, Src: Netgear_d5:d6:80 (20:0c:c8:d5:d6:80), Dst: ca:a7:f4:6f:ac:a8 (ca:a7:f4:6f:ac:a8)


