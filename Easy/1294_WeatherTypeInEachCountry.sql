-- Write an SQL query to find the type of weather in each country for November 2019.
-- The type of weather is:
-- Cold if the average weather_state is less than or equal 15,
-- Hot if the average weather_state is greater than or equal to 25, and
-- Warm otherwise.
-- Return result table in any order.
select c.country_name,
    case
        when avg(w.weather_state) <= 15 then 'Cold'
        when avg(w.weather_state) >= 25 then 'Hot'
        else 'Warm'
    end as weather_type
from Countries c,
    Weather w
where c.country_id = w.country_id
    and left(w.day, 7) = '2019-11'
group by c.country_id;