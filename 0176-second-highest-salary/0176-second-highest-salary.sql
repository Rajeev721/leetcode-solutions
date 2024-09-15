-- Write your PostgreSQL query statement below
select coalesce( max(salary), null) as SecondHighestSalary from employee where salary < ( select max(salary) from employee)