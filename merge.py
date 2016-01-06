#!/usr/bin/python
#-*-coding:utf-8-*-

import os
import time

DIR = "/home/xlore/server36/Mention_Entity/"
m_e_c = {}
delete = 0

start = time.time()
for fn in os.listdir(DIR):
    fn = DIR+fn
    for line in open(fn):
        try:
            m,e = line.strip("\n").split("\t")
            e = e.lower().strip()
            m = m.strip().strip("\t")
            if len(m) < 3:
                print "Too Short:",line.strip("\n")
                delete += 1
                continue
        except Exception,er:
            print er
            print line
        e_c = m_e_c.get(m,{})
        e_c[e] = e_c.get(e,0)+1
        m_e_c[m] = e_c

with open("/home/xlore/server36/Mention_Title_Count.dat","w") as f:
    for m, e_c in m_e_c.items():
        for e,c in e_c.items():
            f.write(m+"::;"+e+"::;"+str(c)+"\n")
            f.flush()

print 'Delete', delete
print time.time()-start
