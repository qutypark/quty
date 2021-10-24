--Return the first non-null value in a list:

-- the net price of the product D is null which seems not correct. 
-- The issue is the discount of the product D is null, 
-- therefore when we take the null value to calculate the net price, PostgreSQL returns null.

-- The get the right price, we need to assume that if the discount is null, it is zero. 
-- Then we can use the COALESCE function as follows:

SELECT
	product,
	(price - COALESCE(discount,0)) AS net_price
FROM
	items;
