-- Report for every three line segments whether they can form a triangle.

-- Return the result table in any order.

-- The result format is in the following example.

select x, y, z, 
    case when x+y>z and x+z>y and y+z>x then 'Yes' else 'No' end as triangle
from triangle
