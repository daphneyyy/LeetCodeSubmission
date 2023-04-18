-- Write an SQL query to report the difference between the number of apples and oranges sold each day.

-- Return the result table ordered by sale_date.

with apple as (
  select sale_date, sold_num
  from Sales
  where fruit = "apples"
  group by sale_date
), 
orange as (
  select sale_date, sold_num
  from Sales
  where fruit = "oranges"
  group by sale_date
)
select a.sale_date, (a.sold_num - o.sold_num) as diff
from apple a
left join orange o on a.sale_date = o.sale_date
