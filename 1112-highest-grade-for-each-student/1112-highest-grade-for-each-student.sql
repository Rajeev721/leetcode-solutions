-- Write your PostgreSQL query statement below
-- with cte as (select student_id,course_id,grade, rank() over(partition by student_id order by grade desc, course_id asc) as rnk from enrollments)

-- select student_id,course_id,grade from cte where rnk = 1

select s.student_id,min(course_id) as course_id,s.grade from enrollments s join (select student_id, max(grade) as grade from enrollments group by student_id) e 
on s.student_id = e.student_id and s.grade = e.grade
group by s.student_id, s.grade