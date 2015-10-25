#!/usr/bin/python
#-*- coding:utf-8 -*-

import sys
import re

from textwithlinks import text_with_links

#LINK_REG = r"""
#  \[\[(:?Bestand|Categorie): (\[\[.*?\]\]|.)*?\]\]
#  | \[\[[a-z]{2,}:.*?\]\]                 # interwiki links
#  """
LINK_REG = r'\[\[(?!File:|Image:|Special:)(.+?)\]\]'
TITLE_REG= r'<title>(.+?)</title>'
#REDIRECT_REG= r'<redirect title="(.+?)" \/>|\{\{redirect|(.+?)\}\}'
REDIRECT_REG= r'<redirect title="(.+?)" \/>'

title = None
for line in sys.stdin:
    res = re.search(TITLE_REG, line)
    if res:
        title = res.group(1)
        print ("%s\t%s\t%s")%(title, title, 1)           # Title
    else:
        res = re.search(REDIRECT_REG, line)
        if res:
            print ("%s\t%s\t%s")%(title, res.group(1), 1) #Redirect Page
        #else: # Hyperlinks
        #    for item in re.findall(LINK_REG, line):
        #        e, m = None, None
        #        if '|' in item:
        #            its = item.split('|')
        #            if len(its) > 2:
        #                continue
        #            if len(its[1]) == 0:
        #                e = m = its[0]
        #            else:
        #                e, m = its
        #            print ("%s\t%s\t%s")%(e, m, 1)
        #        else:
        #            print ("%s\t%s\t%s")%(item, item, 1)

#print re.findall(LINK_REG, '[[sub-Saharan Africa]], where suitable [[habitat]] ')

