-- create table

create table `test`	(
`id` int,
`lastname` varchar(255),
`firstname` varchar(255),
`city` varchar(255),
`purchase` int
);

-- create table (primary , foreign)

create table `test_1`(
`orderid` int not null,
`ordernumber` int not null,
`personid` int,
primary key(`orderid`),
FOREIGN KEY(`personid`) REFERENCES `test`(`id`)
);


-- information_schema.columns

SELECT *
FROM INFORMATION_SCHEMA.COLUMNS
WHERE table_name = 'test';


-- alter table

Alter table `test`
add `email` varchar(255) not null;

alter table `test`
drop column `city`;

  -- Doing multiple ALTER COLUMN actions inside a single ALTER TABLE statement is not possible.
  -- You can do multiple ADD or multiple DROP COLUMN, but just one ALTER COLUMN.

  -- 1. modify -> one by one
alter table `test`
modify `id` int not null;

alter table `test`
modify `firstname` varchar(255) not null;

alter table `test`
modify `lastname` varchar(255) not null;

alter table `test`
modify `city`  varchar(255) not null;

alter table `test`
modify `purchase` int not null;

  -- +) modify value type
alter table `test`
modify `id` varchar(255) not null;
 
  -- 2. add / delete -> multiple
  
alter table `test`
add `address` varchar(255) not null,
add `nickname` varchar(255) not null,
drop column `lastname`;

  -- 3. constraint 
  -- 3.1 unique --> +) primary key
    -- 1) add unique constraint
    alter table `test`
    add unique(id);
    -- 2) drop unique constraint
    alter table `test`
    drop index `id`;
 
 -- 3.2 primary/foreign
    -- 1) add primary key
    alter table `test`
    add primary key(id);
    
    -- 1) add foreign key
    alter table `test_1`
    add foreign key(`personid`) references `test`(`id`);  
    
    -- 2) drop primary key
    alter table `test`
    DROP PRIMARY KEY;
  
    -- 2) drop foreign key 
    -- * table constraint명을 알아야 함
   
    select *
    from inforamion_schema.table_constraints
    where table_name = `test_1`;
    
    alter table `test_1`
    drop foreign key test_1_ibfk_1;
    
 -- 3.3 auto_increment (for primary key)
    --1) lock tables for both primary key table and foreign key table
    LOCK TABLES test_1 write;
    lock tables test write;
    
    --2) drop foreign constraint
    alter table test_1
    drop foreign key test_1_ibfk_1;
    
    --3) alter table add auto_increment
    alter table test
    modify id int not null auto_increment;
    
    --4) unlock table
    unlock tables;
    
    --5) return foreign key
    alter table test_1
    add foreign key(personid) references test(id);
    

-- 4. insert into
    --0)
    insert into test_1 (orderid, ordernumber, personid)
    value (123, 500, 123), (124, 600, 124);
    
    --1) with foreign key
    INSERT INTO test_1
    set ordernumber = 500,
    personid=(select id from test where nickname = 'jihe');


-- 5. delete from table  / truncate table 

    truncate table test_1;
    -- delete * from test_1  is not working
    
    delete from test_1
    where orderid=1;

-- 6. drop table

drop table test_1;
drop table test;







