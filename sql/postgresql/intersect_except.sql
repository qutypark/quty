-- intersect
-- To get popular films which are also top rated films

SELECT *
FROM most_popular_films 
INTERSECT
SELECT *
FROM top_rated_films;

-- except
-- find the top-rated films that are not popular:

SELECT * FROM top_rated_films
EXCEPT 
SELECT * FROM most_popular_films
ORDER BY title;
