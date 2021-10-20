
-- To remove all data from a table, you use the DELETE statement. 
-- However, when you use the DELETE statement to delete all data from a table that has a lot of data, 
-- it is not efficient. 
-- In this case, you need to use the TRUNCATE TABLE statement:


-- To remove data from a table and other tables that have foreign key reference the table, 
-- you use CASCADE option in the TRUNCATE TABLE statement as follows :

TRUNCATE TABLE table_name 
CASCADE;

-- delete

DELETE FROM table_name
WHERE id = 10;

