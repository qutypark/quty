-- finds the films whose lengths are greater than or equal to the maximum length of any film category

SELECT title
FROM film
WHERE length >= ANY(
    SELECT MAX( length )
    FROM film
    INNER JOIN film_category USING(film_id)
    GROUP BY  category_id );
    
    
-- = any    =   in     
