SELECT 
    o."Customer_ID", o."Customer_Name", c."Age", o."City", o."State", o."Region", o."Profit"
FROM orders AS o
INNER JOIN customers AS c
    ON o."Customer_ID" = c."Customer_ID"
WHERE o."Profit" > 1000
