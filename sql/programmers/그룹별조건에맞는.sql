with max_review as (
    select member_id, row_number() over (order by cnt desc) rn
from (
SELECT
    member_id
    , count(distinct review_id) cnt
from rest_review
group by 1
)tmp
)

select
    m.member_name, rr.review_text, rr.review_date
from member_profile m
join rest_review rr on m.member_id =rr.member_id
where m.member_id in (select member_id from max_review where rn = 1)
order by 3
