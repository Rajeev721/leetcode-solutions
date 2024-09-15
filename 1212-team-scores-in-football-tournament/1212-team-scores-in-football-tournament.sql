-- Write your PostgreSQL query sta(tement below
select team_id, team_name,sum(coalesce(num_points ,0)) as num_points  from teams
left join (select host_team , case when host_goals > guest_goals then 3 when host_goals < guest_goals then 0 else 1 end as num_points  FROM matches 
union all 
select guest_team  , case when host_goals < guest_goals then 3 when host_goals > guest_goals then 0 else 1 end as num_points  FROM matches  ) A on team_id = host_team  
group by team_id, team_name
order by num_points desc, team_id asc
