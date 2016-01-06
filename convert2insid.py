#!/usr/bin/python

INSTANCE_LIST = "/home/xlore/XloreData/etc/ttl/xlore.instance.list.ttl"
MENTION_ENTITY="/home/xlore/server36/Mention_Entity_Count.dat"
MENTION_TITLE="/home/xlore/server36/Mention_Title_Count.dat"

d = {}
for line in open(INSTANCE_LIST):
    if "rdfs:label" in line:
        label = line.split('"')[1]
        _id = line[1:line.index('>')]
        d[label.lower()] = _id
        #print _id, label

fw = open(MENTION_ENTITY, "w")
for line in open(MENTION_TITLE):
    try:
        m, t, c = line.strip('\n').split('::;')
        if t == 'deep learning':
            print line
    except:
        continue
    if t.lower() in d:
        #print t
        fw.write("%s::;%s::;%s\n"%(m, d[t.lower()], c))
        fw.flush()
fw.close()



