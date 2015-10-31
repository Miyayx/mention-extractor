DROP TABLE mention_entity_count2;
CREATE TABLE mention_entity_count32(
id int NOT NULL AUTO_INCREMENT,
mention varchar(3000),
entity varchar(100),
count int(6),
PRIMARY KEY(id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE index m_index on mention_entity_count32(mention);

load data local infile "Mention_Entity_Count.dat" into table mention_entity_count32 character set utf8 FIELDS terminated by '::;' (mention,entity,count);
