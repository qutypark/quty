-- The NULLIF function returns a null value if argument_1 equals to argument_2, 
-- otherwise it returns argument_1.

-- First, the NULLIF function returns a null value if the excerpt is empty, otherwise it returns the excerpt. 
-- The result of the NULLIF function is used by the COALESCE function.
-- Second, the COALESCE function checks if the first argument, which is provided by the NULLIF function, 
-- if it is null, then it returns the first 40 characters of the body; otherwise it returns the excerpt in case the excerpt is not null.

SELECT
	id,
	title,
	COALESCE (
		NULLIF (excerpt, ''),
		LEFT (body, 40)
	)
FROM
	posts;
  
  
-- division by zero error

-- 1: male, 2 female
-- when there is no female member --> division zero error 
-- The NULLIF function checks if the number of female members is zero, it returns null. 
-- The total of male members is divided by a null value returns a null value, which is correct.

SELECT
(
SUM (CASE WHEN gender = 1 THEN 1 ELSE 0 END)
/ NULLIF (SUM (CASE WHEN gender = 2 THEN 1 ELSE 0 END),0)
) 
* 100 AS "Male/Female ratio"
FROM
	members;
