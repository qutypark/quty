-- creates a new table called film_r that contains films with the rating R and rental duration 5 days from the film table.

SELECT
    film_id,
    title,
    rental_rate
INTO TABLE film_r
FROM
    film
WHERE
    rating = 'R'
AND rental_duration = 5
ORDER BY
    title;
    
    
-- create table as

CREATE TABLE film_r AS
SELECT
    film_id,
    title,
    rental_rate
FROM
    film
WHERE
    rating = 'R'
AND rental_duration = 5
ORDER BY
    title;
  
-- create table as + with Column Aliases

CREATE TABLE IF NOT EXISTS film_rating (rating, film_count) 
AS 
SELECT
    rating,
    COUNT (film_id)
FROM
    film
GROUP BY
    rating;
    
    
