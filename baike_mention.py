#!/usr/bin/python
#-*- coding:utf-8 -*-

import re 

BAIDU = "/Users/Miyayx/server36/baikedump/baidu-dump-20150702.dat"
HUDONG = "/Users/Miyayx/server36/baikedump/hudong-dump-20150702.dat"


baidu = {}
title = None
_id = None
for line in open(BAIDU):
    line = line.strip()
    if line.startswith('Title'):
        title = line[line.index(': ')+1:]
    if line.startswith('URL:'):
        _id = line.strip()[line.index('/view/'):]
        print _id
        baidu[_id] = title

print "Dictionary finish, length:", len(baidu)

for line in open(BAIDU):
    if line.startswith('FullText:'):
        for item in re.findall(r'\[\[(.+?)\]\]'):
            m, _id = item.split('|')
            print ("%s\t%s")%(baidu[_id], m)

    
