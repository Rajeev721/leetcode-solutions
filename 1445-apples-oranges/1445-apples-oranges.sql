-- Write your PostgreSQL query statement below
with temp as (select sale_date, fruit, sold_num, rank() over(partition by sale_date order by sale_date,fruit asc) as rnk from sales)

select t1.sale_date, t1.sold_num - t2.sold_num diff from temp t1 join temp t2 on t1.sale_date = t2.sale_date 
and t1.rnk+1 = t2.rnk