-- Write an SQL query to find the number of times each student attended each exam.
-- Return the result table ordered by student_id and subject_name.
select a.student_id,
    a.student_name,
    b.subject_name,
    count(e.subject_name) as attended_exams
from Students a
    join Subjects b
    left join Examinations e on a.student_id = e.student_id
    and b.subject_name = e.subject_name
group by a.student_id,
    a.student_name,
    b.subject_name
order by student_id,
    subject_name