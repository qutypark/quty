-- returns the average lengths of all films grouped by film rating:

SELECT
    film_id,
    title,
    length
FROM
    film
WHERE
    length > ALL (
            SELECT
                ROUND(AVG (length),2)
            FROM
                film
            GROUP BY
                rating
    )
ORDER BY
    length;
