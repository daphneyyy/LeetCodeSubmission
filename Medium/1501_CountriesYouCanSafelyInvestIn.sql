-- A telecommunications company wants to invest in new countries. The company intends to invest in the countries where the average call duration of the calls in this country is strictly greater than the global average call duration.
-- Write an SQL query to find the countries where this company can invest.
-- Return the result table in any order.
with codes as (
    select a.id,
        b.name,
        b.country_code
    from Person a
        left join Country b on left(a.phone_number, 3) = b.country_code
)
select c.name as country
from codes c
    join Calls d on c.id = d.caller_id
    or c.id = d.callee_id
group by c.country_code,
    c.name
having avg(d.duration) > (
        select avg(duration)
        from Calls
    );