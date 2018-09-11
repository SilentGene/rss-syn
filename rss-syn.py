#!/usr/bin/python3

__author__ = 'Heyu Lin'

import os
import hashlib
import requests
import time

rss_local = 'environmental-microbiology.rss'
rss_url = 'https://www.nature.com/subjects/environmental-microbiology.rss'
rss_file = requests.get(rss_url)

time_now = time.asctime(time.localtime(time.time()))

if not os.path.exists(rss_local):
    with open(rss_local, 'wb') as f:
        f.write(rss_file.content)
    with open('history.log', 'a') as flog:
        flog.write('{0}\t{1}\n'.format(time_now, 'init'))
else:
    md5_new = hashlib.md5(rss_file.content.decode("utf8").encode("utf8")).hexdigest()
    md5_old = hashlib.md5(rss_local.encode("utf8")).hexdigest()
    if md5_new != md5_old:
        with open(rss_local, 'wb') as f:
            f.write(rss_file.content)
        with open('history.log', 'a') as flog:
            flog.write('{0}\t{1}\n'.format(time_now, 'updated'))
    else:
        with open('history.log', 'a') as flog:
            flog.write('{0}\t{1}\n'.format(time_now, 'NC'))
