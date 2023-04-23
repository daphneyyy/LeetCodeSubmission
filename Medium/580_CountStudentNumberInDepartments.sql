-- Write an SQL query to report the respective department name and number of students majoring in each department for all departments in the Department table (even ones with no current students).

-- Return the result table ordered by student_number in descending order. In case of a tie, order them by dept_name alphabetically.

select d.dept_name, count(s.student_id) as student_number
from Department d
left join Student s on d.dept_id = s.dept_id
group by d.dept_id
order by student_number desc, dept_name 
