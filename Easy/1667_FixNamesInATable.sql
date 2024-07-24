-- Write a solution to fix the names so that only the first character is uppercase and the rest are lowercase.

-- Return the result table ordered by user_id.
  
select user_id, 
    concat(
        upper(substr(name, 1, 1)),
        lower(substr(name, 2))
    ) as name
from users
order by user_id
