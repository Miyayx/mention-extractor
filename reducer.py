#!/usr/bin/python
#-*- coding:utf-8 -*-

from operator import itemgetter
import sys

current_entity = None
current_mention = None
current_count = 0
entity = None
mention = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    entity, mention, count = line.split('\t', 2)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
    # count was not a number, so silently
    # ignore/discard this line
         continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_entity == entity and current_mention == mention:
        current_count += count
    else:
        if current_entity:
            # write result to STDOUT
            print '%s\t%s\t%s' % (current_entity, current_mention, current_count)
        current_count = count
        current_entity = entity
        current_mention = mention

# do not forget to output the last word if needed!
if current_entity:
    print '%s\t%s\t%s' % (current_entity, current_mention, current_count)
