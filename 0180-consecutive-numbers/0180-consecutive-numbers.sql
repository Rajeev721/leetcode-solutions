-- Write your PostgreSQL query statement below

with temp as (select num, lag(num) over(order by id) as prev, lead(num) over(order by id) as rev from logs)

select distinct num ConsecutiveNums  from temp where num = prev and num = rev