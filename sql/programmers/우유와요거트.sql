select cart_id
from 
(select distinct(cart_id), name from cart_products where name in ('Milk','Yogurt')) as tmp
group by cart_id
having count(*) = 2
order by cart_id;

/*
other ans
*/


/*
subquery
*/

select cart_id
from cart_products
where name = 'Yogurt' and
cart_id in (select cart_id from cart_products where name ='Milk')
order by cart_id;

/*
inner join
*/

select a.cart_id
from cart_products as a inner join cart_products as b
on a.cart_id = b.cart_id
where a.name="Milk" and b.name='Yogurt'
order by cart_id;

/*
group_concat
*/

SELECT cart_id from(select cart_id, group_concat(distinct name) as NAME 
from cart_products group by cart_id) as tmp
 where NAME like '%Milk%' and NAME like '%Yogurt%'
 order by cart_id;
