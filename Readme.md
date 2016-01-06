# XLore Entity Mention Extraction

## Online Wikis
* enwiki
* zhwiki
* baidu
* hudong

## Types
* Title
* Redirect Pages(only in wikipedia) [[https://en.wikipedia.org/w/index.php?title=Microsoft_Corporation&redirect=no]]
* Disambiguation Pages[[https://en.wikipedia.org/wiki/Michael_Jordan_(disambiguation)]]
* Hyperlinks in Content

##Code
* Extract Mention~Title
** baidu,hudong baike_mention.py
    `python baike_mention.py > data/Mention_Entity/baidu_mention_entity.dat`
** enwiki,zhwiki mapper.py
    `less enwiki-dump-xxxx.xml.bz2 | python mapper.py > data/Mention_Entity/enwiki_mention_entity.dat`
    `less zhwiki-dump-xxxx.xml.bz2 | python mapper.py > data/Mention_Entity/zhwiki_mention_entity.dat`
* Merge
    `python merge.py`

## Database
>> 10.1.1.36 keg 
>> ./loadToMysql.sql


