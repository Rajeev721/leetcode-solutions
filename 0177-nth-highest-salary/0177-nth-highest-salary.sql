CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
SELECT distinct A.salary FROM (
    SELECT E.salary,
    RANK() OVER(ORDER BY E.salary DESC) AS RNK
    FROM EMPLOYEE E
) A
WHERE A.RNK = N
      
  );
END;
$$ LANGUAGE plpgsql;