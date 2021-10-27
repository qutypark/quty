-- https://www.testdome.com/questions/47159


with cte AS (
  select r.name as region, 
  (case when sum(ifnull(s.amount,0))=0 then 0 else 
                        sum(ifnull(s.amount,0))/count(distinct e.id) end) as avg_sales


	from regions r
	left join states st on r.id = st.regionid
	left join employees e on st.id = e.stateid
	left join sales s on e.id = s.employeeid
	group by r.id, r.name)
 
 select region, avg_sales, (select max(avg_sales) from cte) - avg_sales as diff
 from cte
group by region



