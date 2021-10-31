-- convert data type

SELECT
   CAST ('2015-01-01' AS DATE),
   CAST ('01-OCT-2015' AS DATE);
   
-- cast operator " :: "

SELECT '15 minute'::interval,
 '2 hour'::interval,
 '1 day'::interval,
 '2 week'::interval,
 '3 month'::interval;


-- Now, we have to convert all values in the rating column into integers, 
-- all other A, B, C ratings will be displayed as zero. 
-- To do this, you use the CASE expression with the type CAST as shown in the following query:

SELECT
	id,
	CASE
		WHEN rating~E'^\\d+$' THEN
			CAST (rating AS INTEGER)
		ELSE
			0
		END as rating
FROM
	ratings;

