-- Write an SQL query to report the IDs of the transactions with the maximum amount on their respective day. If in one day there are multiple such transactions, return all of them.
-- Return the result table ordered by transaction_id in ascending order.
select transaction_id
from Transactions
where (date(day), amount) in (
        select date(day) as day_only,
            max(amount) as max_am
        from Transactions
        group by day_only
    )
order by transaction_id