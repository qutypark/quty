SELECT
    distinct order_id
    , product_id, out_date
    , case when out_date <= date('2022-05-01') then '출고완료'
           when out_date > date('2022-05-01') then '출고대기'
           else '출고미정' end as "출고여부"
from food_order
order by 1
