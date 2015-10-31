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
* baidu,hudong baike_mention.py
    `python baike_mention.py > data/Mention_Entity/baidu_mention_entity.dat`
* enwiki,zhwiki mapper.py
    `less enwiki-dump-xxxx.xml.bz2 | python mapper.py > data/Mention_Entity/enwiki_mention_entity.dat`
* merge
    `python merge.py`

## Database
>> 10.1.1.36 keg keg123456
>> ./loadToMysql.sql


