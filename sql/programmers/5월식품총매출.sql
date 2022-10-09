-- 코드를 입력하세요
SELECT
    fp.product_id, fp.product_name, sum(fo.amount)*price as rev
from food_order fo
join food_product fp on fo.product_id = fp.product_id
    # and year(fo.produce_date) = 2022 and month(fo.produce_date) = 5
    and date_format(fo.produce_date, "%Y/%m") = "2022/05"
group by 1, 2
order by rev desc
