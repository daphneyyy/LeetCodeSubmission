-- Write an SQL query to find for each month and country, the number of transactions and their total amount, the number of approved transactions and their total amount.

-- Return the result table in any order.

-- The query result format is in the following example.

# Write your MySQL query statement below
select left(t.trans_date, 7) as month, t.country, count(*) as trans_count, 
sum(t.state = "approved") as approved_count, 
sum(t.amount) as trans_total_amount, 
sum(case 
    when t.state = 'approved' then t.amount 
    else 0 
    end
    ) as approved_total_amount
from Transactions t
group by month, country;