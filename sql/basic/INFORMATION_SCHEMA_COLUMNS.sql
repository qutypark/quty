/*
column name
*/

SELECT COLUMN_NAME
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'tablename'

/*
column loc
*/

SELECT ordinal_position
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'tablename'

/*
nullable
*/

SELECT is_nullable
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'tablename'


/*
data type
*/

SELECT data_type
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'tablename'

