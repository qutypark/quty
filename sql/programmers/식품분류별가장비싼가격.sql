with tmp as (
SELECT
    *
    , max(price) over (partition by category) mp
from food_product 
where category in ('과자', '국', '김치', '식용유')
)

select
    category, price as max_price, product_name
from tmp
where price = mp
order by price desc
