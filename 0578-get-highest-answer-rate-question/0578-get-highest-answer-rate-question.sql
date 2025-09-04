-- Write your PostgreSQL query statement below
select question_id survey_log
from surveyLog
group by 1
order by count(answer_id)*1.0/count(*) desc, 1
limit 1