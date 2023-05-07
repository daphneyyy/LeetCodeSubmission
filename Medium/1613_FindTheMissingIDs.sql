-- Write an SQL query to find the missing customer IDs. The missing IDs are ones that are not in the Customers table but are in the range between 1 and the maximum customer_id present in the table.
-- Notice that the maximum customer_id will not exceed 100.
-- Return the result table ordered by ids in ascending order.
with recursive temp (ids) as (
    select 1
    union all
    select ids + 1
    from temp
    where ids < (
            select max(customer_id)
            from customers
        )
)
select ids
from temp
where ids not in (
        select customer_id as ids
        from customers
    )