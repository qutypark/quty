-- create table

create table `test`	(
`id` int,
`lastname` varchar(255),
`firstname` varchar(255),
`city` varchar(255),
`purchase` int
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





