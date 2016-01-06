#!/usr/bin/python
#-*- coding:utf-8 -*-

import sys
import re

"""
Usage: python mention_extractor.py << less wikidump.xml
"""

#LINK_REG = r"""
#  \[\[(:?Bestand|Categorie): (\[\[.*?\]\]|.)*?\]\]
#  | \[\[[a-z]{2,}:.*?\]\]                 # interwiki links
#  """
#LINK_REG = r'\[\[(?!File:|Image:|Special:)(.+?)\]\]'
LINK_REG = r'\[\[([^\[\]]*)\]\]'
TITLE_REG= r'<title>(.+?)</title>'
#REDIRECT_REG= r'<redirect title="(.+?)" \/>|\{\{redirect|(.+?)\}\}'
REDIRECT_REG= r'<redirect title="(.+?)" \/>'

class Extractor:
    def __init__(self):
        pass 

    def extract(self, stdin):
        title = None
        for line in stdin:
            if '</page>' == line:
                title = None
                continue

            title = get_title(line) 
            print ("%s\t%s")%(title.lower(), title)

            if title:
                if '(disambiguation)' in title:
                    mention = title[:title.index('(disambiguation)')]
                    print ("%s\t%s")%(mention.lower(), title)

                if u'(消歧义)' in title:
                    mention = title[:title.index(u'(消歧义)')]
                    print ("%s\t%s")%(mention.lower(), title)

                continue
            mention = redirect(line)
            if mention:
                print ("%s\t%s")%(mention.lower(), title)
            else: # Hyperlinks
                if "[[" in line and "]]" in line:
                    hyperlinks(line)

    def get_title(line):
        res = re.search(TITLE_REG, line)
        if res:
            return res.group(1)

    def redirect(line):
        res = re.search(REDIRECT_REG, line)
        if res:
            return res.group(1) #Redirect Page

    def hyperlinks(line):
        for item in re.findall(LINK_REG, line):
            e, m = None, None
            if '|' in item:
                its = item.split('|')
                if len(its) > 2:
                    continue
                if len(its[1]) == 0:
                    e = m = its[0]
                else:
                    e, m = its
                print ("%s\t%s")%(m.lower(), e)
            else:
                print ("%s\t%s")%(item.lower(), item)

if __name__=="__main__":
    ex = Extractor()
    ex.extract(sys.stdin)

