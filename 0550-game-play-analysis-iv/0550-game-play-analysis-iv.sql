-- Write your PostgreSQL query statement below
with first_login as (select player_id, min(event_date) as first_login from activity
group by 1
)

select round(count(1) filter(where event_date = first_login +1 ) * 1.0/count(distinct e.player_id),2) as fraction  from activity e join first_login f
on e.player_id =f.player_id 