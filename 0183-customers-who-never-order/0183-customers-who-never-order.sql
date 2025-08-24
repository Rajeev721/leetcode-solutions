-- Write your PostgreSQL query statement below
select name as Customers  from customers c where not exists(select 1 from orders where c.id = customerID)