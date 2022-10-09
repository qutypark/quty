with tmp as (
SELECT
    *, max(favorites) over (partition by food_type) mx_fv
from rest_info
)
select
    food_type, rest_id, rest_name, favorites
from tmp
where favorites = mx_fv
order by 1 desc
