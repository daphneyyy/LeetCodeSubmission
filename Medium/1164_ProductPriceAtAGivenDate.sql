-- Write an SQL query to find the prices of all products on 2019-08-16. Assume the price of all products before any change is 10.
-- Return the result table in any order.
select *
from (
        select b.product_id,
            10 as price
        from Products b
        group by b.product_id
        having min(b.change_date) > '2019-08-16'
        union
        select p.product_id,
            p.new_price as price
        from Products p
        where p.change_date <= '2019-08-16'
            and (p.product_id, p.change_date) in (
                select product_id,
                    max(change_date) as change_date
                from Products
                where change_date <= '2019-08-16'
                group by product_id
            )
    ) temp
group by temp.product_id