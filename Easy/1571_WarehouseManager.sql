-- Write an SQL query to report the number of cubic feet of volume the inventory occupies in each warehouse.

-- Return the result table in any order.

-- The query result format is in the following example.

with product_volume as (
    select p.product_id, p.Width * p.Length * p.Height as volume
    from Products p
)
select w.name as warehouse_name, sum(w.units * p.volume) as volume
from Warehouse w, product_volume p
where w.product_id = p.product_id
group by w.name;