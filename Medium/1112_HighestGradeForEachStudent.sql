-- Write a SQL query to find the highest grade with its corresponding course for each student. In case of a tie, you should find the course with the smallest course_id.
-- Return the result table ordered by student_id in ascending order.
with temp as (
    select student_id,
        max(grade) as grade
    from Enrollments
    group by student_id
)
select t.student_id,
    min(e.course_id) as course_id,
    e.grade
from Enrollments e
    right join temp t on e.student_id = t.student_id
    and e.grade = t.grade
group by e.student_id
order by student_id;