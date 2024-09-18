# Write your MySQL query statement below

SELECT REQUEST_AT AS Day,round(SUM(CASE WHEN STATUS = 'completed' then 0 else 1 end)/count(*),2) AS `Cancellation Rate` FROM 
TRIPS JOIN USERS ON TRIPS.CLIENT_ID = USERS.USERS_ID
JOIN USERS AS USERS1 ON TRIPS.driver_id  = USERS1.USERS_ID
WHERE USERS.BANNED = 'No' AND USERS1.BANNED = 'No'
and request_at between "2013-10-01" and "2013-10-03"
group by request_at