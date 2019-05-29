#!/usr/bin/env python3

#A script that checks the date key of all the entries in the mpd database,
#and makes a bar graph about the results.
#-dmh 20190529

import mpd
import numpy as np
import matplotlib.pyplot as plt
def connect_client():
    """Connect to MPD Client"""
    client = mpd.MPDClient()
    client.connect("localhost", 6600)
    return client

#let's start by doing it just with the current playlist before we quadrispaz
#everything by going through the whole database.
client = connect_client()
raw_dates = []


for song in client.playlistinfo():
    try:
        raw_dates.append(song["date"][:4])
    except:
        pass
raw_dates.sort()
unique_dates = np.unique(raw_dates)

date_dict = {}
for unique_date in unique_dates:
   date_dict[unique_date] = 0 

for raw_date in raw_dates:
    date_dict[raw_date] += 1

print(date_dict)

plt.figure(num=1, figsize=(14,5))
plt.style.use('ggplot')
plt.bar(date_dict.keys(),date_dict.values())
plt.xticks(rotation=45)
plt.show()
