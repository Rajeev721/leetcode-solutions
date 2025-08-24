-- Write your PostgreSQL query statement below
select name as results from (select name , count(rating) from Users join MovieRating using (user_id)
group by 1
order by 2 desc, 1 asc
limit 1)
union all

select title as results from (select title, avg(rating) from Movies join MovieRating using (movie_id)
where created_at between '2020-02-01' and '2020-02-28'
group by 1
order by 2 desc, 1 asc
limit 1)