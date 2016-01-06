#!/usr/bin/python
#-*- coding:utf-8 -*-

import re 

"""
URL: http://baike.baidu.com/view/6858.htm#sub5564900
"""

BAIDU = "/home/keg/data/baikedump/baidu-dump-20151029.dat"
HUDONG = "/home/keg/data/baikedump/hudong-dump-20150702.dat"


def baidu_mention():
    """
    baidu提取了title和hyperlink
    """
    baidu = {}
    title = None
    _id = None
    #for line in open(BAIDU):
    fr = open(BAIDU)
    line = fr.readline()
     
    ### 创建baidu与其id的对应字典
    ### 同时输出title\ttitle
    while line:
        line = line.strip('\n')
        if line.startswith('Title'):
            try:
                title = line[line.index(': ')+2:]
                print ("%s\t%s"%(title, title))
                while not line.startswith('URL:'):
                    line = fr.readline()
                if line.startswith('URL:'):
                    _id = '/'+line.strip('\n').split('/',3)[-1]
                    if '#sub' in _id:
                        _id=('/'.join(_id.split('.htm#sub'))+'.htm').replace('view', 'subview')
                        #print _id
                    baidu[_id] = title
            except:
                line = fr.readline()
                continue
        line = fr.readline()
    
    print "Dictionary finish, length:", len(baidu)
    
    for line in open(BAIDU):
        if line.startswith('FullText:'):
            for item in re.findall(r'\[\[(.+?)\]\]', line):
                #print item
                try:
                    m, _id = item.split('||')
                except:
                    continue
                if _id in baidu:
                    print ("%s\t%s")%(m, baidu[_id]) #mention, entity
                else:
                    #print "Missing id:%s"%_id
                    continue

def hudong_mention():
    """
    hudong只提取了title
    """
    for line in open(HUDONG):
        if line.startswith('Title:'):
            title = line.strip('\n').split(':', 1)[1]
            print ("%s\t%s"%(title, title))

if __name__=="__main__":
    hudong_mention()
    baidu_mention()
    
        
