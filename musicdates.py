#!/usr/bin/env python3

#A script that checks the date key of all the entries in the mpd database,
#and makes a bar graph about the results.
#-dmh 20190529

import mpd
import numpy as np
import matplotlib.pyplot as plt
import re

def connect_client():
    """Connect to MPD Client"""
    client = mpd.MPDClient()
    client.connect("localhost", 6600)
    return client

client = connect_client()

raw_dates = client.list("date")
clean_dates = []
pattern = '^[0-9]{4}'
for date in raw_dates:
    clean_date = re.findall(pattern, date)
    if clean_date:
        clean_dates.append(clean_date[0])

unique_dates=np.unique(clean_dates)
date_dict = {}

for unique_date in unique_dates:
   date_dict[unique_date] = int(client.count("date",unique_date)['songs'])

print(date_dict)

plt.figure(num=1, figsize=(16,6))
plt.style.use('ggplot')

x_positions=[]
count=1
for date in unique_dates:
    x_positions.append(count)
    count += 1

bar_heights=list(date_dict.values())
plt.bar(x_positions, bar_heights)
plt.xticks( x_positions,unique_dates, rotation=45)
plt.ylabel('number of music files')
plt.title('Music Files By Year Of Release')

plt.show()
